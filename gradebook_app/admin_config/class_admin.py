from django.contrib import admin

from gradebook_app.admin_config.action_column_mixin import ActionsColumnMixin
from gradebook_app.forms import ClassForm

"""this py file is for future development to modify 'Class' in admin site"""


class ClassAdmin(ActionsColumnMixin, admin.ModelAdmin):
    """for now, this class is used to "assign/remove/change/show a lecturer to a class" in the admin page"""
    list_display = ('number', 'course', 'semester', 'lecturer', 'actions_column')
    search_fields = ('number', 'course__title', 'semester__name', 'lecturer__name')
    form = ClassForm

