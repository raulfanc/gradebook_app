- More real-world approach, to manage User, and User Groups, for example, if registered user need to choose different usergroups to do different permissions
- This allows you to add any extra fields or methods to your user model as needed without having to rely on signals or other workarounds.

1.  Create a new app (if you don't already have one) for handling user-related models and authentication:
```terminal
python manage.py startapp users
```
2.  In the new app's `models.py`, create a custom user model that inherits from `AbstractBaseUser` and `PermissionsMixin`. You can add any additional fields to this model as needed. Here's an example:
```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
```
3.  Update the `AUTH_USER_MODEL` setting in your project's `settings.py` to point to your custom user model:
```python
AUTH_USER_MODEL = 'users.CustomUser'
```
4.  Update your `Student` and `Lecturer` models in the `models.py` file to include a OneToOne relationship with the custom user model:
```python
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    # ...

class Lecturer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lecturer_profile')
    # ...
```
5.  Update your forms and views to work with the custom user model. Replace all instances of `User` with `get_user_model()` and make necessary changes to field names (e.g., change `username` to `email`).
    
6.  Run `python manage.py makemigrations` and `python manage.py migrate` to apply the changes to the database.
    
7.  Update the admin panel to use the custom user model:
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import Student, Lecturer

CustomUser = get_user_model()

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Lecturer)
```

This code defines the CustomUserAdmin class, which inherits from the default UserAdmin. It customizes the list_display, search_fields, and ordering attributes to work with the custom user model. It also updates the fieldsets and add_fieldsets to display the appropriate fields in the admin forms.

Finally, the CustomUser, Student, and Lecturer models are registered with the admin site. Now, you should be able to create and manage users, students, and lecturers through the admin panel with the custom user model.