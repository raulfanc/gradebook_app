from django.contrib import admin
from django.urls import path

from gradebook_app import views
from gradebook_app.admin_config.action_column_mixin import ActionsColumnMixin

"""this py file is for future development to modify 'Student' in admin site"""


class StudentAdmin(ActionsColumnMixin, admin.ModelAdmin):
    """for now, this class is used to "add/remove/show students"  and help "upload_students" in the admin page"""
    list_display = ('firstname', 'lastname', 'email', 'DOB', 'actions_column')
    search_fields = ('firstname', 'lastname', 'email')

    def get_urls(self):
        """avoid "pk redirect", use get_urls() to add a custom url to the admin page for uploading students"""
        urls = super().get_urls()
        custom_urls = [
            path('upload_students/', self.admin_site.admin_view(views.upload_students), name='upload_students'),
        ]
        return custom_urls + urls


