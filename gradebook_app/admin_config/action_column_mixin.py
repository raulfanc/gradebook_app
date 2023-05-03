# admin_config/action_column_mixin.py
from django.urls import reverse
from django.utils.html import format_html


class ActionsColumnMixin:
    """This mixin is used to add an 'Action' column to the admin list_display"""
    """simplify the code in admin_config/xxx_admin.py for two customizing buttons"""
    def actions_column(self, obj):
        update_url = reverse(f"admin:gradebook_app_{obj._meta.model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:gradebook_app_{obj._meta.model_name}_delete", args=[obj.pk])
        return format_html(
            '<a class="button update-button" href="{}">Update</a> '
            '<a class="button delete-button" href="{}">Delete</a>',
            update_url, delete_url
        )

    actions_column.short_description = 'Action'
