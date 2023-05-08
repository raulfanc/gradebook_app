import pandas as pd
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

from django.contrib import messages

from django.shortcuts import render

from gradebook_app.forms import *


@staff_member_required
def upload_students(request):
    if request.method == 'POST':
        file = request.FILES['file']

        # Read the Excel file
        df = pd.read_excel(file)

        # Process each row
        for index, row in df.iterrows():
            # Get the values from the Excel file
            first_name = row['firstname']
            last_name = row['lastname']
            username = row['username']
            email = row['email']
            dob = row['dob']
            group_name = row['group'].lower()

            # Check if the username already exists in the database
            if User.objects.filter(username=username).exists():
                continue  # Skip adding this student

            # Set the default password
            default_password = '60x5x9rc'

            # Create a new user with the default password
            user = User.objects.create_user(username, email, default_password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if group_name == 'student':
                Student.objects.create(user=user, firstname=first_name, lastname=last_name, email=email, DOB=dob)
            elif group_name == 'lecturer':
                Lecturer.objects.create(user=user, firstname=first_name, lastname=last_name, email=email, DOB=dob)

        messages.success(request, 'Students have been uploaded successfully.')
        return HttpResponseRedirect(reverse('admin:gradebook_app_student_changelist'))
    else:
        return render(request, 'admin/gradebook_app/student/upload_student_form.html')
