from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash


def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # acquire data from the form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # checks if the inputted passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        # check if the inputted username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        # check if the inputted email exists
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
        # creates the User object
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')

    return render(request, 'register.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')


def edit_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        current_username = request.user.username

        if new_username == current_username:
            messages.error(request, 'You already took that username')
            return redirect('profile')
        elif User.objects.filter(username=new_username).exists():
            messages.error(request, 'Username already taken')
            return redirect('profile')
        else:
            user = request.user
            user.username = new_username
            user.save()
            messages.success(request, 'Username updated')
            return redirect('profile')
    else:
        messages.error(request, 'Error occurred')
        return redirect('profile')


def edit_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('new_email')
        current_email = request.user.email

        if new_email == current_email:
            messages.error(request, 'You are already using that email')
            return redirect('profile')
        elif User.objects.filter(email=new_email).exists():
            messages.error(request, 'Email already taken')
            return redirect('profile')
        else:
            user = request.user
            user.email = new_email
            user.save()
            messages.success(request, 'Email has been updated')
            return redirect('profile')
    else:
        messages.error(request, 'Error occurred')
        return redirect('profile')


def edit_personal_info(request):
    if request.method == 'POST':
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')

        current_first_name = request.user.first_name
        current_last_name = request.user.last_name

        if new_first_name == current_first_name and new_last_name == current_last_name:
            messages.error(request, 'You are already using the first name and last name')
            return redirect('profile')
        else:
            user = request.user
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.save()
            messages.success(request, 'Personal information has been updated')
            return redirect('profile')
    else:
        messages.error(request, 'Error occurred')
        return redirect('profile')


def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if new_password != confirm_new_password:
            messages.error(request, 'New passwords do not match')
            return redirect('profile')
        elif old_password == new_password:
            messages.error(request, 'Old password and new password are the same')
            return redirect('profile')
        else:
            user = request.user
            if not user.check_password(old_password):
                messages.error(request, 'Old password is incorrect')
                return redirect('profile')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
    else:
        messages.error(request, 'Error occurred')
        return redirect('profile')


def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        if not request.user.check_password(password):
            messages.error(request, 'Password is incorrect')
            return redirect('profile')
        else:
            request.user.delete()
            logout(request)
            return redirect('login')

    return redirect('profile')


def logout_user(request):
    logout(request)
    return redirect('login')
