# semester_admin.py
from django.contrib import admin

from gradebook_app.admin_config.action_column_mixin import ActionsColumnMixin


class SemesterAdmin(ActionsColumnMixin, admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'actions_column')
    search_fields = ('name',)
