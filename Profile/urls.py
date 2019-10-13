from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('myProfile',views.Profile_view,name='profile_view'),
    path('update',views.update,name='update_profile'),
    
   
]