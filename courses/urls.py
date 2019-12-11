from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('courselist',views.courses,name='course_list'),
    # WEB AS WELL AS API ENDPOINT
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
    #API ENDPOINTS
    path('CreateUser',views.CreateUser.as_view(),name='CreateUser'),
    path('LoginUser',views.LoginUser.as_view(),name='LoginUser'),
    path('CourseListView',views.CourseListView.as_view(),name='CourseListView'),
    path('TutorToken',views.TutorToken,name='TutorToken'),
    path('CourseDetail',views.CourseDetail.as_view(),name='CourseDetail'),
    path('CreateCourse',views.CreateCourse.as_view(),name='CreateCourse'),
    path('CreateVideo',views.CreateVideo.as_view(),name='CreateVideo'),
    path('CreateProblem',views.CreateProblem.as_view(),name='CreateProblem'),
    path('UpdateCourse/<int:pk>',views.UpdateCourse.as_view(),name='UpdateCourse'),
    path('UpdateVideo/<int:pk>',views.UpdateVideo.as_view(),name='UpdateVideo'),





   


    
    
    
    
    

    
    

   
    
   
]
