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
    path('tutor',views.tutor,name='tutor'),
    path('publish',views.publish,name='publish'),
    path('Published',views.Published,name='published'),
    path('add_desc',views.add_desc,name='add_desc'),
    path('myPublication',views.myPublication,name='myPublication'),
    path('add_video',views.add_video,name='add_video'),
    path('problem_publish/<int:obj_id>',views.problem_publish,name='problem_publish'),
    path('video_add/<int:obj_id>',views.video_add,name='video_add'),
    path('submit/<int:obj_id>',views.submit,name='submit'),
    path('mysubmission<int:obj_id>',views.mysubmission,name="mysubmission"),

    
    

   
    
   
]