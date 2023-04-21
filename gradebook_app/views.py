"""
View for the administrator to enroll/remove/show students in classes.
View for the administrator to upload students from excel files to the website.
View for the system to email students when their marks are ready.
View for the lecturer to log in to the gradebook.
View for the lecturer to enter students' marks in the gradebook.
View for the student to log in to the gradebook.
View for the students to view their marks in the gradebook.

views.py is working with forms.py and models.py to create the views for the administrator and the lecturer.
"""
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from .forms import *


class HomePageView(TemplateView):
    template_name = 'gradebook_app/home.html'


# ==============administrator to create/update/delete/show semesters================
class SemesterListView(ListView):
    model = Semester


class SemesterDetailView(DetailView):
    model = Semester


class SemesterCreateView(CreateView):
    model = Semester
    form_class = SemesterForm


class SemesterUpdateView(UpdateView):
    model = Semester
    form_class = SemesterForm


class SemesterDeleteView(DeleteView):
    model = Semester
    success_url = reverse_lazy('semester_list')
# =============================end====================================


# ==========administrator to create/update/delete/show courses========
class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
# ===========================end======================================


# ==========administrator to create/update/delete/show classes========
class ClassListView(ListView):
    model = Class


class ClassDetailView(DetailView):
    model = Class


class ClassCreateView(CreateView):
    model = Class
    form_class = ClassForm


class ClassUpdateView(UpdateView):
    model = Class
    form_class = ClassForm
# ===========================end========================================


# ==========administrator to create/update/delete/show lecturers========
class LecturerListView(ListView):
    model = Lecturer


class LecturerDetailView(DetailView):
    model = Lecturer


class LecturerCreateView(CreateView):
    model = Lecturer
    form_class = LecturerForm


class LecturerUpdateView(UpdateView):
    model = Lecturer
    form_class = LecturerForm


class LecturerDeleteView(DeleteView):
    model = Lecturer
    success_url = reverse_lazy('lecturer_list')
#=========================End=======================================


# ==========administrator to create/update/delete/show students========
class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
# ===========================End=============================================


##=====================proper permissions and checks=============================
class LecturerRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='lecturer').exists()))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class StudentRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='student').exists()))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
# ==========================End=============================================


# ==============================Enrolment================================
class EnrolmentCreateView(CreateView):
    model = Enrolment
    form_class = EnrolmentForm


class EnrolmentListView(LecturerRequiredMixin, ListView):
    model = Enrolment

    def get_queryset(self):
        """
        Filter out the enrolments that belong to classes taught by the lecturer.
        - Lecturers can only see enrolments of their own classes.
        - The lecturer's classes will be stored in the session.
        - If the lecturer has no classes, the lecturer will be redirected to the home page (handled by html).
        """
        queryset = super().get_queryset()
        lecturer_classes = Class.objects.filter(lecturer=self.request.user.lecturer_profile)
        has_classes = lecturer_classes.exists()
        self.request.session['has_classes'] = has_classes
        return queryset.filter(enrolled_class__in=lecturer_classes)


class StudentEnrolmentListView(StudentRequiredMixin, ListView):
    model = Enrolment
    template_name = 'gradebook_app/student_enrolment_list.html'

    def get_queryset(self):
        """same as above list view, but for STUDENTs"""
        queryset = super().get_queryset()
        student_enrolments = queryset.filter(enrolled_student=self.request.user.student_profile)
        self.request.session['has_enrolments'] = student_enrolments.exists()
        return student_enrolments


class EnrolmentDetailView(StudentRequiredMixin, DetailView):
    model = Enrolment
    template_name = 'gradebook_app/view_grade.html'

    def get_queryset(self):
        """same as the above code"""
        queryset = super().get_queryset()
        return queryset.filter(enrolled_student=self.request.user.student_profile)



class EnrolmentUpdateView(LecturerRequiredMixin, UpdateView):
    model = Enrolment
    form_class = EnrolmentForm
    template_name = 'gradebook_app/enrolment_update.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(enrolled_class__lecturer=self.request.user.lecturer_profile)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print(f"Enrolment ID: {obj.pk}, Student: {obj.enrolled_student}, Class: {obj.enrolled_class}")
        return obj

    def get_success_url(self):
        return reverse_lazy('enrolment_list')


class EnrolmentDeleteView(DeleteView):
    model = Enrolment
    success_url = reverse_lazy('enrolment_list')
# =====================================End=================================================


# ==============================Register and Profile Update================================
# Views for authentication's register
def register(request):
    """
    Create a view that allows users to register
    :param request: the request sent to the server
    :return: If the request method is GET, returns a blank registration form.
             If the request method is POST and the form is valid, creates a new user, logs the user in,
             and redirects them to the update_user_info page to complete their profile.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('update_user_info')  # Redirect to the update_user_info view
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def update_user_info(request):
    """
    A view that allows registered users to update their personal information.
    If the request method is POST, the function creates a UserUpdateForm instance with the data from the request,
    and checks if it's valid. If the form is valid, it saves the changes to the user's information and redirects
    the user to the 'home' page.
    If the request method is GET, the function creates a UserUpdateForm instance with the current user's information,
    it is used to display the form with the user's current information for the first time the page is loaded.
    :param request: The HTTP request object.
    :return: A rendered HTML response containing a UserUpdateForm.
    """
    user = request.user
    if user.groups.filter(name="student").exists():
        initial_form_class = StudentForm
    elif user.groups.filter(name="lecturer").exists():
        initial_form_class = LecturerForm
    else:
        initial_form_class = UserUpdateForm

    if request.method == 'POST':
        form = initial_form_class(request.POST, instance=user)
        if form.is_valid():
            instance = form.save(commit=False)
            group = form.cleaned_data.get('group')
            if group:
                user.groups.set([group])  # Set the selected group
            instance.user = user
            instance.save()
            return redirect('home')
    else:
        form = initial_form_class(instance=user)
    return render(request, 'registration/update_user_info.html', {'form': form})

# ====================================End=======================================================


# ====================================Email====================================================
@login_required
@user_passes_test(lambda u: u.groups.filter(name='lecturer').exists())
def send_email(request, enrolment_id):
    """
    Send an email to the student
    :param request: normal request
    :param enrolment_id: the id of the enrolment linked to the enrolled student and assigned lecturer
    :return: redirect to the enrolment list page
    """
    enrolment = get_object_or_404(Enrolment, pk=enrolment_id)
    student_email = enrolment.enrolled_student.email
    subject = "Your Grade is Available"
    message = f"Dear {enrolment.enrolled_student},\n\nYour grade for {enrolment.enrolled_class} is now available. Please log in to the Gradebook to view your grade.\n\nBest regards,\n{enrolment.enrolled_class.lecturer}\nLecturer"
    from_email = None  # Uses the default email in settings.py

    try:
        send_mail(subject, message, from_email, [student_email])
        messages.success(request, f"Email sent to {enrolment.enrolled_student}.")
    except Exception as e:
        messages.error(request, str(e))

    return redirect('enrolment_list')
# ================================end============================================
