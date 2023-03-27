"""
Enrollment model can be handled by Django's built-in ManyToManyField `Student` and `Class` models.
Tag model can be handled by Django's built-in ManyToManyField 'Course' model.
"""

from django import forms
from .models import Semester, Course, Class, Lecturer, Student


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'start_date', 'end_date', 'year']


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


