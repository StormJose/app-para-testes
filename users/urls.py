# users/urls.py (or your project's urls.py)

from django.contrib.auth import views as auth_views
from .views import register, profile
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
