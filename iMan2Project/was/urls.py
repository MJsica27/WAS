from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_user, name='logout'),
]