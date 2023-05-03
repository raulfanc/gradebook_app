from django.contrib import admin

from django.urls import reverse
from django.utils.html import format_html

"""this py file is for future development to modify 'Enrolment' in admin site"""


class EnrolmentAdmin(admin.ModelAdmin):
    """"for now, this class is used to "enrol/remove/show student to classes" in the admin page"""
    # list_display = ('enrolled_student', 'enrolled_class', 'enrollment_date', 'action_button')
    list_display = ('enrolled_student', 'enrolled_class', 'enrollment_date', 'actions_column')
    search_fields = ('student__name', 'enrolled_class__number')

    # def delete_button(self, obj):
    #     """original way to add an 'Action' button to the admin list_display, i.e., delete button"""
    #     url = reverse("admin:gradebook_app_enrolment_delete", args=[obj.pk])
    #     return format_html('<a class="button" href="{}">Delete</a>', url)
    #
    # delete_button.short_description = 'Action'

    def actions_column(self, obj):
        """initially coded to add an 'Actions' column to the admin list_display"""
        """only this `enrolment` class is coded as is, the rest of classes using <ActionsColumnMixin.py>"""
        update_url = reverse("admin:gradebook_app_enrolment_change", args=[obj.pk])
        delete_url = reverse("admin:gradebook_app_enrolment_delete", args=[obj.pk])
        return format_html(
            '<a class="button update-button" href="{}">Update</a> '
            '<a class="button delete-button" href="{}">Delete</a>',
            update_url, delete_url
        )

    actions_column.short_description = 'Action'





