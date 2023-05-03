from django.contrib import admin

from gradebook_app.models import Semester, Course, Class, Lecturer, Student, Enrolment
from gradebook_app.admin_config.enrolment_admin import EnrolmentAdmin
from gradebook_app.admin_config.student_admin import StudentAdmin
from gradebook_app.admin_config.class_admin import ClassAdmin
from gradebook_app.admin_config.course_admin import CourseAdmin
from gradebook_app.admin_config.lecturer_admin import LecturerAdmin
from gradebook_app.admin_config.semester_admin import SemesterAdmin

from django.urls import path

# from gradebook_app.models import Semester, Course, Class, Lecturer, Student, Enrolment
# from . import views
# from .forms import ClassForm
#
#
# class EnrollmentAdmin(admin.ModelAdmin):
#     """"this class is used to "enrol/remove/show student to classes" in the admin page"""
#     list_display = ('enrolled_student', 'enrolled_class', 'enrollment_date')
#     search_fields = ('student__name', 'enrolled_class__number')
#
#
# class StudentAdmin(admin.ModelAdmin):
#     """"this class is used to "add/remove/show students"  and help "upload_students" in the admin page"""
#     list_display = ('firstname', 'lastname', 'email', 'DOB')
#     search_fields = ('firstname', 'lastname', 'email')
#
#     def get_urls(self):
#         """avoid "pk redirect", use get_urls() to add a custom url to the admin page for uploading students"""
#         urls = super().get_urls()
#         custom_urls = [
#             path('upload_students/', self.admin_site.admin_view(views.upload_students), name='upload_students'),
#         ]
#         return custom_urls + urls

#
# class ClassAdmin(admin.ModelAdmin):
#     """this class is used to "assign/remove/change/show a lecturer to a class" in the admin page"""
#     list_display = ('number', 'course', 'semester', 'lecturer')
#     search_fields = ('number', 'course__title', 'semester__name', 'lecturer__name')
#     form = ClassForm


# Register your models here.
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrolment, EnrolmentAdmin)
