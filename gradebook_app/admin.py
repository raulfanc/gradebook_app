from django.contrib import admin

from gradebook_app.models import Semester, Course, Class, Lecturer, Student, Enrolment
from .forms import ClassForm


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrolled_student', 'enrolled_class', 'enrollment_date')
    search_fields = ('student__name', 'enrolled_class__number')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'DOB')
    search_fields = ('firstname', 'lastname', 'email')


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
