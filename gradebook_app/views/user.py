from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gradebook_app.forms import *


# Views for authentication's register
def register(request):
    """
    Create a view that allows users to register
    :param request: the request sent to the server
    :return: If the request method is GET, returns a blank registration form.
             If the request method is POST and the form is valid, creates a new user, logs the user in,
             and redirects them to the update_user_info page to complete their profile.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('update_user_info')  # Redirect to the update_user_info view
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def update_user_info(request):
    """
    A view that allows registered users to update their personal information.
    If the request method is POST, the function creates a UserUpdateForm instance with the data from the request,
    and checks if it's valid. If the form is valid, it saves the changes to the user's information and redirects
    the user to the 'home' page.
    If the request method is GET, the function creates a UserUpdateForm instance with the current user's information,
    it is used to display the form with the user's current information for the first time the page is loaded.
    :param request: The HTTP request object.
    :return: A rendered HTML response containing a UserUpdateForm.
    """
    user = request.user
    if user.groups.filter(name="student").exists():
        initial_form_class = StudentForm
    elif user.groups.filter(name="lecturer").exists():
        initial_form_class = LecturerForm
    else:
        initial_form_class = UserUpdateForm

    if request.method == 'POST':
        form = initial_form_class(request.POST, instance=user)
        if form.is_valid():
            instance = form.save(commit=False)
            group = form.cleaned_data.get('group')
            if group:
                user.groups.set([group])  # Set the selected group
            instance.user = user
            instance.save()
            return redirect('home')
    else:
        form = initial_form_class(instance=user)
    return render(request, 'registration/update_user_info.html', {'form': form})