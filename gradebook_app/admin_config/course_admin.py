# course_admin.py
from django.contrib import admin

from gradebook_app.admin_config.action_column_mixin import ActionsColumnMixin


class CourseAdmin(ActionsColumnMixin, admin.ModelAdmin):
    list_display = ('title', 'code', 'description', 'actions_column')
    search_fields = ('title', 'code')

