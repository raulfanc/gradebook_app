from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from gradebook_app.models import Semester
from gradebook_app.forms import SemesterForm


class HomePageView(TemplateView):
    template_name = 'gradebook_app/home.html'


# ==============administrator to create/update/delete/show semesters================
"""only used semester for testing purpose for generic views"""


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


"""========below generic views are not developed yet================"""

# # ==========administrator to create/update/delete/show courses========

# class CourseListView(ListView):
#     model = Course
#
#
# class CourseDetailView(DetailView):
#     model = Course
#
#
# class CourseCreateView(CreateView):
#     model = Course
#     form_class = CourseForm
#
#
# class CourseUpdateView(UpdateView):
#     model = Course
#     form_class = CourseForm
# ===========================end======================================
#
#
# # ==========administrator to create/update/delete/show classes========

# class ClassListView(ListView):
#     model = Class
#
#
# class ClassDetailView(DetailView):
#     model = Class
#
#
# class ClassCreateView(CreateView):
#     model = Class
#     form_class = ClassForm
#
#
# class ClassUpdateView(UpdateView):
#     model = Class
#     form_class = ClassForm
# # ===========================end========================================
#
#
# # ==========administrator to create/update/delete/show lecturers========

# class LecturerListView(ListView):
#     model = Lecturer
#
#
# class LecturerDetailView(DetailView):
#     model = Lecturer
#
#
# class LecturerCreateView(CreateView):
#     model = Lecturer
#     form_class = LecturerForm
#
#
# class LecturerUpdateView(UpdateView):
#     model = Lecturer
#     form_class = LecturerForm
#
#
# class LecturerDeleteView(DeleteView):
#     model = Lecturer
#     success_url = reverse_lazy('lecturer_list')
# # =========================End=======================================
#
#
# # ==========administrator to create/update/delete/show students========

# class StudentListView(ListView):
#     model = Student
#
#
# class StudentDetailView(DetailView):
#     model = Student
#
#
# class StudentCreateView(CreateView):
#     model = Student
#     form_class = StudentForm
#
#
# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentForm
#
#
# class StudentDeleteView(DeleteView):
#     model = Student
#     success_url = reverse_lazy('student_list')
# # ===========================End=============================================
