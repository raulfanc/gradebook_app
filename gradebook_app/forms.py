"""
Enrollment model can be handled by Django's built-in ManyToManyField `Student` and `Class` models.
"""

from django.forms import DateInput
from django.core.validators import EmailValidator, RegexValidator
from django import forms
from django.contrib.auth.models import Group
from django.db import transaction

from .models import *


class SemesterForm(forms.ModelForm):
    """
    This form is used to create a new semester.
    name: The name of the semester, combine with year, e.g. "semester 1 - 2023", "semester 2 - 2023".
    name: instead of taking an input, change it to a dropdown menu with options associate with 'name'.
    start_date: The start date of the semester.
    end_date: The end date of the semester.

    """
    class Meta:
        model = Semester
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

    # use this to control the front end form display to 'form-control'
    def __init__(self, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'description']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'course', 'semester', 'lecturer', 'students']
        labels = {
            'lecturer': 'Lecturer (Set to blank to remove assigned lecturer)',
        }


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['user', 'firstname', 'lastname', 'email', 'course', 'DOB']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'firstname', 'lastname', 'email', 'DOB']


# Customised User Creation Form with validation
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z]+$', 'Enter a valid first name (letters only)')]
    )
    last_name = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z]+$', 'Enter a valid last name (letters only)')]
    )
    email = forms.EmailField(required=True, validators=[EmailValidator()])
    group = forms.ModelChoiceField(queryset=Group.objects.filter(name__in=['student', 'lecturer']), required=True)
    DOB = forms.DateField(
        required=True,
        widget=DateInput(attrs={'type': 'date'}),
        label='Date of Birth'
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=commit)
        group = self.cleaned_data.get('group')
        user.groups.add(group)

        if group.name == 'lecturer':
            Lecturer.objects.create(user=user, firstname=user.first_name, lastname=user.last_name, email=user.email, DOB='1970-01-01')  # Replace with actual DOB
        elif group.name == 'student':
            Student.objects.create(user=user, firstname=user.first_name, lastname=user.last_name, email=user.email, DOB='1970-01-01')  # Replace with actual DOB

        return user


# used views.py, EnrolmentForm is used to enrol a Lecturer into a class
class EnrolmentForm(forms.ModelForm):
    class Meta:
        model = Enrolment
        fields = ['enrolled_student', 'enrolled_class', 'grade', 'grade_date']


# used views.py, EnrolmentStudentForm is used to enrol a Student into a class
class EnrolmentStudentForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['students']
