from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_username', views.edit_username, name='edit_username'),
    path('profile/edit_email', views.edit_email, name='edit_email'),
    path('profile/edit_personal_info', views.edit_personal_info, name='edit_personal_info'),
    path('profile/change_password', views.change_password, name='change_password'),
    path('courses/', views.courses, name='courses'),
    path('courses/add_course', views.add_course, name='add_course'),
    path('courses/<int:course_id>/details', views.course_details, name='course_details'),
    path('courses/<int:course_id>/details/edit_course', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/details/delete_course', views.delete_course, name='delete_course'),
    path('courses/<int:course_id>/details/add_schedule', views.add_schedule, name='add_schedule'),
    path('courses/<int:course_id>/details/<int:schedule_id>/delete_schedule', views.delete_schedule, name='delete_schedule'),
    path('courses/<int:course_id>/tasks', views.course_tasks, name='course_tasks'),
    path('courses/<int:course_id>/tasks/<int:task_id>/view', views.view_selected_task, name='view_selected_task'),
    path('courses/<int:course_id>/tasks/add_task', views.add_task, name='add_task'),
    path('courses/<int:course_id>/tasks/<int:task_id>/view/edit_task', views.edit_selected_task, name='edit_selected_task'),
    path('courses/<int:course_id>/tasks/<int:task_id>/view/complete_task', views.complete_task, name='complete_task'),
    path('courses/<int:course_id>/tasks/<int:task_id>/view/delete_task', views.delete_task, name='delete_task'),
    path('courses/<int:course_id>/tasks/<int:task_id>/view/update_score', views.update_task_score, name='update_task_score'),
    path('courses/<int:course_id>/grade', views.course_grade, name='course_grade'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_user, name='logout'),
]
