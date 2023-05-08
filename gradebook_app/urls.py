from django.urls import path
from gradebook_app.views import enrolment, user, send_email, generic_views

urlpatterns = [
    path('', generic_views.HomePageView.as_view(), name='home'),
    path('accounts/register/', user.register, name='register'),
    path('accounts/update_user_info/', user.update_user_info, name='update_user_info'),

    # Semester URLs
    path('semesters/', generic_views.SemesterListView.as_view(), name='semester_list'),
    path('semesters/<int:pk>/', generic_views.SemesterDetailView.as_view(), name='semester_detail'),
    path('semesters/add/', generic_views.SemesterCreateView.as_view(), name='semester_create'),
    path('semesters/<int:pk>/edit/', generic_views.SemesterUpdateView.as_view(), name='semester_update'),
    path('semesters/<int:pk>/delete/', generic_views.SemesterDeleteView.as_view(), name='semester_delete'),

    path('lecturer_enrolment_list/', enrolment.LecturerEnrolmentListView.as_view(), name='lecturer_enrolment_list'),
    path('lecturer_enrolment_update/<int:pk>/', enrolment.LecturerEnrolmentUpdateView.as_view(),
         name='lecturer_enrolment_update'),
    path('student_enrolment_list/', enrolment.StudentEnrolmentListView.as_view(), name='student_enrolment_list'),
    path('student_enrolment_detail/<int:pk>/', enrolment.StudentEnrolmentDetailView.as_view(),
         name='student_enrolment_detail'),
    path('send_email/<int:enrolment_id>/', send_email.send_email, name='send_email'),

    # ==================below are urls' routes for generic views, not developed yet===================
    # Course URLs
    # path('courses/', views.CourseListView.as_view(), name='course_list'),
    # path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    # path('courses/add/', views.CourseCreateView.as_view(), name='course_create'),
    # path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_update'),
    #
    # # Class URLs
    # path('classes/', views.ClassListView.as_view(), name='class_list'),
    # path('classes/<int:pk>/', views.ClassDetailView.as_view(), name='class_detail'),
    # path('classes/add/', views.ClassCreateView.as_view(), name='class_create'),
    # path('classes/<int:pk>/edit/', views.ClassUpdateView.as_view(), name='class_update'),

    # Lecturer URLs
    # path('lecturers/', views.LecturerListView.as_view(), name='lecturer_list'),
    # path('lecturers/<int:pk>/', views.LecturerDetailView.as_view(), name='lecturer_detail'),
    # path('lecturers/add/', views.LecturerCreateView.as_view(), name='lecturer_create'),
    # path('lecturers/<int:pk>/edit/', views.LecturerUpdateView.as_view(), name='lecturer_update'),
    # path('lecturers/<int:pk>/delete/', views.LecturerDeleteView.as_view(), name='lecturer_delete'),
    #
    # # Student URLs
    # path('students/', views.StudentListView.as_view(), name='student_list'),
    # path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    # path('students/add/', views.StudentCreateView.as_view(), name='student_create'),
    # path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    # path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
