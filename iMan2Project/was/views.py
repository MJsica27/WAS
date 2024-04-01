from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q, Case, When, Value, IntegerField
from .models import Course, Schedule


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('courses')
            else:
                messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('courses')
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
            return render(request, 'register.html')

        # check if the inputted email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return render(request, 'register.html')

        # creates the User object
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()
        messages.success(request, 'Registration successful')
        return redirect('login')

    return render(request, 'register.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')


def courses(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_courses = Course.objects.filter(UserID=user_id).order_by('SubjectCode')
        context = {
            'user_courses': user_courses
        }
        return render(request, 'courses.html', context)
    else:
        return redirect('login')


def course_details(request, course_id):
    if request.user.is_authenticated:
        course = Course.objects.get(CourseID=course_id)

        schedules = Schedule.objects.filter(CourseID=course).order_by(
            Case(
                When(DayOfWeek='Monday', then=Value(1)),
                When(DayOfWeek='Tuesday', then=Value(2)),
                When(DayOfWeek='Wednesday', then=Value(3)),
                When(DayOfWeek='Thursday', then=Value(4)),
                When(DayOfWeek='Friday', then=Value(5)),
                When(DayOfWeek='Saturday', then=Value(6)),
                When(DayOfWeek='Sunday', then=Value(7)),
                default=Value(8),
                output_field=IntegerField(),
            ),
            'StartTime',
        )

        context = {
            'course': course,
            'schedules': schedules,
        }
        return render(request, 'course_details.html', context)
    return redirect('courses')


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
            messages.success(request, 'Account successfully deleted')
            return redirect('login')

    return redirect('profile')


def logout_user(request):
    logout(request)
    return redirect('login')


def add_course(request):
    user = request.user

    if request.method == 'POST':
        subject_code = request.POST.get('subject_code')
        subject_description = request.POST.get('subject_description')
        section = request.POST.get('section')
        professor = request.POST.get('professor')

        if Course.objects.filter(SubjectCode=subject_code, UserID=user).exists():
            messages.error(request, 'Course already added')
        else:
            course = Course.objects.create(UserID=user, SubjectCode=subject_code, SubjectDescription=subject_description, Section=section, Professor=professor)
            course.save()
            messages.success(request, 'Course Added')
            return redirect('courses')

    return redirect('courses')


def edit_course(request, course_id):
    if request.method == 'POST':
        updated_subject_code = request.POST.get('subject_code')
        updated_subject_description = request.POST.get('subject_description')
        updated_section = request.POST.get('section')
        updated_professor = request.POST.get('professor')

        course = Course.objects.filter(CourseID=course_id).first()

        if course:
            if updated_subject_code != course.SubjectCode:
                if Course.objects.filter(SubjectCode=updated_subject_code, CourseID=course_id).exclude(SubjectCode=course.SubjectCode).exists():
                    messages.error(request, 'Subject code already taken')
                    return redirect('course_details', course_id)
                else:
                    course.SubjectCode = updated_subject_code
                    course.SubjectDescription = updated_subject_description
                    course.Section = updated_section
                    course.Professor = updated_professor
                    course.save()
                    messages.success(request, 'Course Updated')
                    return redirect('course_details', course_id)
            else:
                course.SubjectDescription = updated_subject_description
                course.Section = updated_section
                course.Professor = updated_professor
                course.save()
                messages.success(request, 'Course Updated')
                return redirect('course_details', course_id)
        else:
            messages.error(request, 'Course not found')

    return redirect('course_details', course_id)


def delete_course(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(CourseID=course_id)
        course.delete()
        messages.success(request, '')
        return redirect('courses')
    return redirect('courses')


def add_schedule(request, course_id):
    course = Course.objects.get(CourseID=course_id)

    if request.method == 'POST':
        day_of_week = request.POST.get('day_of_week')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        room = request.POST.get('room')

        if Schedule.objects.filter(Q(DayOfWeek=day_of_week) & Q(Room=room) & (
                Q(StartTime=start_time) | Q(EndTime=end_time) |
                Q(StartTime__lte=start_time, EndTime__gte=end_time))).exists():
            messages.error(request, 'Schedule overlaps with existing schedule')
        elif Schedule.objects.filter(Q(CourseID=course) & Q(DayOfWeek=day_of_week) & (
                Q(StartTime__range=(start_time, end_time)) | Q(EndTime__range=(start_time, end_time)))).exists():
            messages.error(request, 'Schedule overlaps with existing schedule')
        else:
            schedule = Schedule.objects.create(CourseID=course, DayOfWeek=day_of_week, StartTime=start_time, EndTime=end_time, Room=room)
            schedule.save()
            messages.success(request, 'Schedule added')
    return redirect('course_details', course_id)


def delete_schedule(request, course_id, schedule_id):
    if request.method == 'POST':
        schedule = Schedule.objects.get(ScheduleID=schedule_id)
        schedule.delete()
        messages.success(request, '')
        return redirect('course_details', course_id)
    return redirect('course_details', course_id)
