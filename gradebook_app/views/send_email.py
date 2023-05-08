from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect

from django.core.mail import send_mail

from gradebook_app.forms import *


@login_required
@user_passes_test(lambda u: u.groups.filter(name='lecturer').exists())
def send_email(request, enrolment_id):
    """
    Send an email to the student
    :param request: normal request
    :param enrolment_id: the id of the enrolment linked to the enrolled student and assigned lecturer
    :return: redirect to the enrolment list page
    """
    enrolment = get_object_or_404(Enrolment, pk=enrolment_id)
    student_email = enrolment.enrolled_student.email
    subject = "Your Grade is Available"
    message = f"Dear {enrolment.enrolled_student},\n\nYour grade for {enrolment.enrolled_class} is now available. Please log in to the Gradebook to view your grade.\n\nBest regards,\n{enrolment.enrolled_class.lecturer}\nLecturer"
    from_email = None  # Uses the default email in settings.py

    try:
        send_mail(subject, message, from_email, [student_email])
        messages.success(request, f"Email sent to {enrolment.enrolled_student}.")
    except Exception as e:
        messages.error(request, str(e))

    return redirect('enrolment_list')