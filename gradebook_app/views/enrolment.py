from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gradebook_app.forms import *
from gradebook_app.views.authorization import LecturerRequiredMixin, StudentRequiredMixin


class LecturerEnrolmentListView(LecturerRequiredMixin, ListView):
    """view enrolled students for the same class that the lecturer teaches"""
    model = Enrolment
    template_name = 'gradebook_app/lecturer_enrolment_list.html'

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


class LecturerEnrolmentUpdateView(LecturerRequiredMixin, UpdateView):
    model = Enrolment
    form_class = LecturerEnrolmentForm
    template_name = 'gradebook_app/lecturer_enrolment_update.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(enrolled_class__lecturer=self.request.user.lecturer_profile)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print(f"Enrolment ID: {obj.pk}, Student: {obj.enrolled_student}, Class: {obj.enrolled_class}")
        return obj

    def get_success_url(self):
        return reverse_lazy('lecturer_enrolment_list')


class StudentEnrolmentListView(StudentRequiredMixin, ListView):
    model = Enrolment
    template_name = 'gradebook_app/student_enrolment_list.html'

    def get_queryset(self):
        """same as above list view, but for STUDENTs"""
        queryset = super().get_queryset()
        student_enrolments = queryset.filter(enrolled_student=self.request.user.student_profile)
        self.request.session['has_enrolments'] = student_enrolments.exists()
        return student_enrolments


class StudentEnrolmentDetailView(StudentRequiredMixin, DetailView):
    model = Enrolment
    # form_class = StudentEnrolmentForm
    template_name = 'gradebook_app/student_enrolment_detail.html'

    # def get_queryset(self):
    #     """same as the above code"""
    #     queryset = super().get_queryset()
    #     return queryset.filter(enrolled_student=self.request.user.student_profile)


class EnrolmentDeleteView(DeleteView):
    model = Enrolment
    success_url = reverse_lazy('lecturer_enrolment_list')


class EnrolmentCreateView(CreateView):
    model = Enrolment
    form_class = LecturerEnrolmentForm
