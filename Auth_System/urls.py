from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
   
   
]
