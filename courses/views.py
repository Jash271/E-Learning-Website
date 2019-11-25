from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from . models import Course,Video,Practice,Tutor,Tag,Submission
from django.contrib.auth.models import User
from django.http import HttpResponse
import pdb
from . forms import ContactForm,ProblemForm,SolutionForm
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
    flag=Video.objects.filter(Course_ID=obj_id).count()
    request.session['course_id']=obj_id
    print(flag)
    print(video)
    return render(request,"Video.html",{'video':video,'flag':flag})


def problem(request,obj_id):
    problem=Practice.objects.filter(Lec_Ref=obj_id)
    return render(request,'Problemset.html',{'problem':problem})

def mycourses(request):
   
    mycourse=Course.objects.filter(Enrollment_ID=request.user)
    return render(request,'mycourse.html',{'mycourse':mycourse})


def tutor(request):
    t1=Tutor(User_Ref=request.user)
    t1.save()
    return HttpResponse("You are now a tutor")
    
def publish(request):
    tags=Tag.objects.all()
    return  render (request,"publish.html",{'tags':tags})

def Published(request):
    Name=request.POST['Name']
    Desc=request.POST['Desc']
    tag=request.POST['Tag']
    request.session['tag10']=request.POST['Tag']
    request.session['Name1']=request.POST['Name']
    request.session['Desc1']=request.POST['Desc']
    
    tag2=tag.strip()
    tag3=tag2.upper()
    tag4=Tag.objects.all()
    for tag4 in tag4:
        tag5=tag4.Name.strip()
        tag6=tag5.upper()
        if tag6==tag3:
            tutor=Tutor.objects.get(User_Ref=request.user)
            
            course=Course(Author=tutor,Name=Name,Desc=Desc)
            course.save()
            course.Tag_ID.add(tag4)
            return redirect('/home')
        else:
            return render (request,"Create_Tag.html")

def add_desc(request):
    desc=request.POST['Desc']
    tag=request.session['tag10']
    tag11=Tag(Name=tag,Desc=desc)
    tag11.save()
    tutor=Tutor.objects.get(User_Ref=request.user)
    course=Course(Author=tutor,Name=request.session['Name1'],Desc=request.session['Desc1'])
    course.save()
    Tag12=Tag.objects.get(Name=tag)
    course.Tag_ID.add(Tag12)
    return redirect('/home')

def myPublication(request):
    tutor=Tutor.objects.get(User_Ref=request.user)
    course=Course.objects.filter(Author_id=tutor)
    return render(request,"course_Publish_List.html",{'course':course})

def add_video(request):
    courseid=request.session['course_id']
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            link=form.cleaned_data.get('Link')
           
            name=form.cleaned_data.get('Name')
            desc=form.cleaned_data.get('Desc')
            course=Course.objects.get(id=courseid)
            tutor=Tutor.objects.get(User_Ref=request.user)
            video=Video(Author=tutor,Name=name,Video_Link=link,Desc=desc,Course_ID=course)
            video.save()
            return redirect('/home')
    else:
        form=ContactForm()
    return render(request,'add_video.html',{'form':form})

def problem_publish(request,obj_id):
    if request.method=='POST':
        form=ProblemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('Name')
            problem_stat=form.cleaned_data.get('Desc')
            video=Video.objects.get(id=obj_id)
            tutor=Tutor.objects.get(User_Ref=request.user)
            problem=Practice(Author=tutor,Lec_Ref=video,Name=name,Desc=problem_stat)
            problem.save()
            return redirect('/home')
    else:
        form=ProblemForm()
    return render(request,'Problem_Publish.html',{'form':form})


def video_add(request,obj_id):
    video=Video.objects.filter(Course_ID=obj_id)
    flag=Video.objects.filter(Course_ID=obj_id).count()
    request.session['course_id']=obj_id
    print(flag)
    print(video)
    return render(request,"Video_myPublished.html",{'video':video,'flag':flag})


def submit(request,obj_id):
    if request.method =='POST':
        form=SolutionForm(request.POST,request.FILES)
        if form.is_valid():
            code_1=form.cleaned_data.get('Code')
            print(code_1)
            ref=Practice.objects.get(id=obj_id)
            print(ref)
            solution=Submission(Author=request.user,Problem_Ref=ref,Code=code_1)
            solution.save()
            return redirect('/home')
    else :
        form=SolutionForm()
    return render (request,"Submission.html",{'form':form})

def mysubmission(request,obj_id):
    
    q_set=Submission.objects.filter(Problem_Ref=obj_id,Author=request.user)
    print(q_set)
    return render(request,"mysubmission.html",{'q_set':q_set})
    








    








            
            




       
    
   
    
    
    
  
   
