"""
Enrollment model can be handled by Django's built-in ManyToManyField `Student` and `Class` models.
Tag model can be handled by Django's built-in ManyToManyField 'Course' model.
"""

from django import forms
from django.forms import DateInput

from .models import Semester, Course, Class, Lecturer, Student


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
        fields = ['name', 'start_date', 'end_date', 'year']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'description', 'tags']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'course', 'semester', 'lecturer', 'students', 'class_code', 'schedule']


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['user', 'bio', 'staffID', 'firstname', 'lastname', 'email', 'course', 'DOB']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'StudentID', 'firstname', 'lastname', 'email', 'DOB']


