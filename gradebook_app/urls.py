from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/update_user_info/', views.update_user_info, name='update_user_info'),

    # Semester URLs
    path('semesters/', views.SemesterListView.as_view(), name='semester_list'),
    path('semesters/<int:pk>/', views.SemesterDetailView.as_view(), name='semester_detail'),
    path('semesters/add/', views.SemesterCreateView.as_view(), name='semester_create'),
    path('semesters/<int:pk>/edit/', views.SemesterUpdateView.as_view(), name='semester_update'),
    path('semesters/<int:pk>/delete/', views.SemesterDeleteView.as_view(), name='semester_delete'),

    # Course URLs
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_update'),

    # Class URLs
    path('classes/', views.ClassListView.as_view(), name='class_list'),
    path('classes/<int:pk>/', views.ClassDetailView.as_view(), name='class_detail'),
    path('classes/add/', views.ClassCreateView.as_view(), name='class_create'),
    path('classes/<int:pk>/edit/', views.ClassUpdateView.as_view(), name='class_update'),

    # Lecturer URLs
    path('lecturers/', views.LecturerListView.as_view(), name='lecturer_list'),
    path('lecturers/<int:pk>/', views.LecturerDetailView.as_view(), name='lecturer_detail'),
    path('lecturers/add/', views.LecturerCreateView.as_view(), name='lecturer_create'),
    path('lecturers/<int:pk>/edit/', views.LecturerUpdateView.as_view(), name='lecturer_update'),
    path('lecturers/<int:pk>/delete/', views.LecturerDeleteView.as_view(), name='lecturer_delete'),

    # Student URLs
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # Enrolment URLs
    path('enrolments/', views.EnrolmentListView.as_view(), name='enrolment_list'),
    path('enter_grade/<int:pk>/', views.EnrolmentUpdateView.as_view(), name='update_grade'),
    path('view_grade/<int:pk>/', views.EnrolmentDetailView.as_view(), name='view_grade'),

]
