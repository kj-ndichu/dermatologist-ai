from django.urls import path
from django.contrib.auth import views as auth_view

from . import views
app_name = "skin_app"
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('submit', views.submit, name='submit'),
    path('profile', views.profile, name="profile"),

    path('login/',  auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', auth_view.LogoutView.as_view(
        template_name="logout.html"), name="logout"),
    path('dashboard', views.dashboard, name='dashboard')
]
