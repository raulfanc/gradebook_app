"""
View for the administrator to create/update/delete/show semesters.
View for the administrator to create/update/delete/show courses (including tags management).
View for the administrator to create/update/delete/show classes.
View for the administrator to create/update/delete/show lecturers.
View for the administrator to assign/remove/change/show lecturers to a class.
View for the administrator to create/update/delete/show students (including student profiles).
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
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Semester, Course, Class, Lecturer, Student
from .forms import SemesterForm, CourseForm, ClassForm, LecturerForm, StudentForm


# Semester views
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


# Course views
class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm


# Class views
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


# Lecturer views
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


# Student views
class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm


# Views for administrators to manage semesters, courses, classes, lecturers, and students
# ... (Similar to the basic views provided in the previous response)

# View for assigning/removing/changing/showing a lecturer to a class
class AssignLecturerView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'gradebook_app.change_class'
    form_class = ClassForm
    template_name = 'gradebook_app/assign_lecturer.html'

    def form_valid(self, form):
        class_obj = Class.objects.get(id=self.kwargs['pk'])
        class_obj.lecturer = form.cleaned_data['lecturer']
        class_obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('class_detail', args=[self.kwargs['pk']])


# View for enrolling/removing/showing students in classes
class EnrollStudentsView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'gradebook_app.change_enrollment'
    form_class = StudentForm
    template_name = 'gradebook_app/enroll_students.html'

    def form_valid(self, form):
        class_obj = Class.objects.get(id=self.kwargs['pk'])
        student = form.cleaned_data['student']
        enrollment = Enrollment(student=student, class_obj=class_obj)
        enrollment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('class_detail', args=[self.kwargs['pk']])


# View for uploading students from excel files
class UploadStudentsView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'gradebook_app.add_student'
    # Implement file uploading, use third-party libraries like openpyxl or pandas
    # to read the excel file and create Student instances
    # ...


# View for emailing students when their marks are ready
class EmailMarksView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'gradebook_app.email_students'
    # Implement emailing students using Django's built-in email support
    # ...


# Views for lecturer and student gradebook login
# Use Django's built-in authentication views to handle lecturer and student logins
# ...


# View for lecturers to enter students' marks in the gradebook
class LecturerEnterMarksView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'gradebook_app.change_enrollment'
    # Implement form handling for entering student marks
    # ...


# View for students to view their marks in the gradebook
class StudentViewMarksView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'gradebook_app/student_view_marks.html'
    context_object_name = 'student'