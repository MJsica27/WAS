from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_username', views.edit_username, name='edit_username'),
    path('profile/edit_email', views.edit_email, name='edit_email'),
    path('profile/edit_personal_info', views.edit_personal_info, name='edit_personal_info'),
    path('profile/change_password', views.change_password, name='change_password'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_user, name='logout'),
]
