from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('courselist',views.courses,name='course_list'),
    path('enroll/<int:obj_id>',views.enroll,name='enroll'),
    path('video/<int:obj_id>',views.video,name='video'),
    path('problem/<int:obj_id>',views.problem,name='problem'),
    path('mycourses',views.mycourses,name='Mycourses'),
   
    
   
]