from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Course,Video,Practice
from django.contrib.auth.models import User

# Create your views here.
def courses(request):
    course=Course.objects.all()
    return render(request,"course_list.html",{'course':course})


def enroll(request,obj_id):
    course=Course.objects.get(id=obj_id)
    course.Enrollment_ID.add(request.user)
    pass
def video(request,obj_id):
    video=Video.objects.filter(Course_ID=obj_id)
    print(video)
    return render(request,"Video.html",{'video':video})
def problem(request,obj_id):
    problem=Practice.objects.filter(Lec_Ref=obj_id)
    return render(request,'Problemset.html',{'problem':problem})

def mycourses(request):
   
    mycourse=Course.objects.filter(Enrollment_ID=request.user)
    return render(request,'mycourse.html',{'mycourse':mycourse})


