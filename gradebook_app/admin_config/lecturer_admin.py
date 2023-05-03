# admin_config/lecturer_admin.py
from django.contrib import admin
from gradebook_app.admin_config.action_column_mixin import ActionsColumnMixin


class LecturerAdmin(ActionsColumnMixin, admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'staffID', 'DOB', 'actions_column')
    search_fields = ('firstname', 'lastname', 'email', 'staffID')
    readonly_fields = ('staffID',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('course')
        return queryset

    def courses(self, obj):
        return ", ".join([course.title for course in obj.course.all()])

    courses.short_description = 'Courses'
