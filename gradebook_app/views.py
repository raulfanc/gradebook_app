"""
according to models.py, we need the following views:
View for the administrator to create/update/delete/show semesters.
View for the administrator to create/update/delete/show courses (including tags management).
View for the administrator to create/update/delete/show classes.
View for the administrator to create/update/delete/show lecturers.
View for the administrator to assign/remove/change/show lecturers to a class.
View for the administrator to create/update/delete/show students (including student profiles).
View for the administrator to enroll/remove/show students in classes.
View for the administrator to upload students from excel files to the website.
View for the system to email students when their marks are ready.
View for the lecturer to log in to the gradebook.
View for the lecturer to enter students' marks in the gradebook.
View for the student to log in to the gradebook.
View for the students to view their marks in the gradebook.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.
# use generic views
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/

def index(request):
    return render(request, 'gradebook_app/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'gradebook_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'gradebook_app/register.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'gradebook_app/change_password.html', {'form': form})

def semester_list(request):
    semesters = Semester.objects.all()
    return render(request, 'gradebook_app/semester_list.html', {'semesters': semesters})

def semester_detail(request, pk):
    semester = Semester.objects.get(pk=pk)
    return render(request, 'gradebook_app/semester_detail.html', {'semester': semester})

def semester_create(request):
    if request.method == 'POST':
        semester_form = SemesterForm(request.POST)
        if semester_form.is_valid():
            semester_form.save()
            return redirect('semester_list')
    else:
        semester_form = SemesterForm()
    return render(request, 'gradebook_app/semester_create.html', {'semester_form': semester_form})

def semester_update(request, pk):
    semester = Semester.objects.get(pk=pk)
    if request.method == 'POST':
        semester_form = SemesterForm(request.POST, instance=semester)
        if semester_form.is_valid():
            semester_form.save()
            return redirect('semester_list')
    else:
        semester_form = SemesterForm(instance=semester)
    return render(request, 'gradebook_app/semester_update.html', {'semester_form': semester_form})

def semester_delete(request, pk):
    semester = Semester.objects.get(pk=pk)
    semester.delete()
    return redirect('semester_list')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'gradebook_app/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'gradebook_app/course_detail.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('course_list')
    else:
        course_form = CourseForm()
    return render(request, 'gradebook_app/course_create.html', {'course_form': course_form})

def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            return redirect('course_list')
    else:
        course_form = CourseForm(instance=course)
    return render(request, 'gradebook_app/course_update.html', {'course_form': course_form})

def course_delete(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('course_list')

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'gradebook_app/class_list.html', {'classes': classes})

def class_detail(request, pk):
    class_ = Class.objects.get(pk=pk)
    return render(request, 'gradebook_app/class_detail.html', {'class_': class_})

def class_create(request):
    if request.method == 'POST':
        class_form = ClassForm(request.POST)
        if class_form.is_valid():
            class_form.save()
            return redirect('class_list')