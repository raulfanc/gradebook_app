from django.contrib import admin
from django.urls import path

from gradebook_app.models import Semester, Course, Class, Lecturer, Student, Enrolment
from . import views
from .forms import ClassForm


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrolled_student', 'enrolled_class', 'enrollment_date')
    search_fields = ('student__name', 'enrolled_class__number')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'DOB')
    search_fields = ('firstname', 'lastname', 'email')

    # use get_urls() to add a custom url to the admin page for uploading students
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload_students/', self.admin_site.admin_view(views.upload_students), name='upload_students'),
        ]
        return custom_urls + urls


class ClassAdmin(admin.ModelAdmin):
    list_display = ('number', 'course', 'semester', 'lecturer')
    search_fields = ('number', 'course__title', 'semester__name', 'lecturer__name')
    form = ClassForm


# Register your models here.
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Class, ClassAdmin)
admin.site.register(Lecturer)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrolment, EnrollmentAdmin)