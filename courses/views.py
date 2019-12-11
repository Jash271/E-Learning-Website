from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from . models import Course,Video,Practice,Tutor,Tag,Submission
from django.contrib.auth.models import User
from django.http import HttpResponse
import pdb
from . forms import ContactForm,ProblemForm,SolutionForm
from . serializer import CourseSerializer,TutorSerializer1,VideoSerializer,CourseSerializer3,VideoEditSerializer,UserSerializer,LoginSerializer,Practiceserializer,CourseSerializer4
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from requests.api import request
from . permission import Permit,Permit1
from rest_framework import permissions
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from django.contrib.auth import logout, authenticate, login
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
import json

# Create your views here.
def courses(request):
    course=Course.objects.all()
    return render(request,"course_list.html",{'course':course})


def enroll(request,obj_id):
    course=Course.objects.get(id=obj_id)
    course.Enrollment_ID.add(request.user)  

    return Response('Enrolled',status=status.HTTP_200_OK)



def video(request,obj_id):
    video=Video.objects.filter(Course_ID=obj_id)
    flag=Video.objects.filter(Course_ID=obj_id).count()
    request.session['course_id']=obj_id
    print(flag)
    print(video)

    return render(request,"Video.html",{'video':video,'flag':flag})


def problem(request,obj_id):
    problem=Practice.objects.filter(Lec_Ref=obj_id )
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
    


#@api_view(['POST'])
#def post(self,request,*args,**Kwargs):
        #u_name=request.data['username']
        #try:
           # User.objects.get(username=u_name)
            #return HttpResponse("User Already  exists")
        #except:
            #serializer=UserSerializer(data=request.data)
            #if serializer.is_valid():
                #serializer.save()
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Create New User (API)
class CreateUser(generics.GenericAPIView):
    permission_classes=[AllowAny]
   
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'CreateUserSerializer.html'
    def get(self,request):
        serializer=UserSerializer
        serializer1=UserSerializer
        return Response({'serializer':serializer})
    def post(self,request):
        u_name=request.data['username']
        try:
            new_user=User.objects.get(username=u_name)
            return JsonResponse('User already exists',safe=False)
        except:
            serializer=UserSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                n_user=User.objects.get(username=u_name)
                
                login(request,n_user)
                response=({'username':u_name,'email':request.data['email']})
                

                return JsonResponse(response,safe=False)
            return Response({'serializer1':serializer})




#Login (API)
class LoginUser(generics.GenericAPIView):
    permission_classes=[AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'LoginUser.html'

    def get(self,request):
        serilaizer=LoginSerializer
        return Response({'serializer':serilaizer})

    
    
    def post(self,request):
        u_name=request.data['username']
        
        passw=request.data['password']
        
    

        try:
            l_user=authenticate(username=u_name,password=passw)
            print(l_user)
            
            login(request,l_user)
            
            return JsonResponse('LoggedIN',safe=False)
        except:
            response=('Username or Password incorrect')
            return JsonResponse(response,safe=False)


#CourseList API
class CourseListView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    
    serializer_class=CourseSerializer
    queryset=Course.objects.all()

#Token Generate API
@login_required
def TutorToken(request):
    l_user=User.objects.get(username=request.user.username)

    try:
       tutor=Tutor.objects.get(User_Ref=l_user)
       token=Token.objects.get(user=request.user)
       print(token.key)
       response=({'token':token.key})
       return JsonResponse(response,safe=False)
    
    except:
        flag=0
        print(flag)
        tutor=Tutor(User_Ref=l_user)
        tutor.save()
        token=Token.objects.create(user=request.user)
        print(token.key)
        response=({'token':token.key})
        return JsonResponse(response,safe=False)
#Course Detail API
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[Permit]
    authentication_classes = [TokenAuthentication]

    serializer_class=CourseSerializer3
    queryset=Course.objects.all()

#Course Create API
class CreateCourse(generics.CreateAPIView):
    permission_classes=[Permit]
    authorzation_classes=[TokenAuthentication]
    serializer_class= CourseSerializer3
    queryset=Course.objects.all()

    def perform_create(self, serializer):
        tutor=Tutor.objects.get(User_Ref=self.request.user)
        serializer.save(Author=tutor)

#Video Create API
class CreateVideo(generics.GenericAPIView):
    permission_classes=[AllowAny]
    authentication_classes=[TokenAuthentication]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'CreateVideoSerializer.html'
    def get(self,request):
        serializer=VideoEditSerializer()
        return Response({'serializer':serializer})
    def post(self,request):
        video_name=request.data['Name']
        video_desc=request.data['Desc']
        video_course=request.data['Course_ID']
        video_link=request.data['Video_Link']
        tutor=Tutor.objects.get(User_Ref=request.user)
        course=Course.objects.get(id=video_course)
        print(course.Author)
        print(course.id)
        print(tutor.User_Ref)
        print(str(course.Author)==str(tutor.User_Ref))
        if str(course.Author)==str(tutor.User_Ref) :

            serializer=VideoEditSerializer(data=request.data)
            if serializer.is_valid():
                print(0)
                video=Video(Name=video_name,Author=tutor,Desc=video_desc,Video_Link=video_link,Course_ID=course)
                video.save()
                response=({'Name':video_name,'Desc':video_desc,'Course':video_course,'Link':video_link})
                return JsonResponse(response,safe=False)


            else:
                serializer1=VideoEditSerializer
                return Response({'serializer1':serializer})
        else:
            return JsonResponse('Plaease Choose Appropriate Course',safe=False)
#Create Video API (2)
"""class CreateVideo(generics.CreateAPIView):
    permission_classes=[Permit1]
    
    serializer_class=VideoEditSerializer
    queryset=Video.objects.all()

    def create(self, request):
        course=request.data['Course_ID']
        print(course)
        tutor=Tutor.objects.get(User_Ref=self.request.user)
        print(tutor.User_Ref)
        flag=0
        course=Course.objects.get(id=course)
        print(course.Author)
        if str(tutor.User_Ref) == str(course.Author):
            flag=1
            serializer=VideoEditSerializer(data=request.data)
            
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_OK)
        else:
            print(flag)
            return Response(status=status.HTTP_400_BAD_REQUEST)"""
#Practice Problem API
class CreateProblem(generics.CreateAPIView):
    permission_classes=[Permit1]
    authentication_classes=[TokenAuthentication]
    serializer_class=Practiceserializer
    queryset=Practice.objects.all()

    def create(self,serializer):
        lec=serializer.data['Lec_Ref']
        tutor=Tutor.objects.get(User_Ref=self.request.user)
        print(tutor.User_Ref)
        flag=0
        video=Video.objects.get(id=lec)
        print(video.Author)
        if tutor.User_Ref==video.Author:
            flag=1
            serializer=VideoEditSerializer(data=self.request.data)
            if serializer.is_valid():

             serializer.save(Author=tutor)
             return Response(status=status.HTTP_201_CREATED)
            else:
             return Response(status=status.HTTP_409_CONFLICT)
            
        else:
            print(flag)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Update Course API
class UpdateCourse(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[Permit1]
    authentication_classes=[TokenAuthentication]
    serializer_class=CourseSerializer4
    queryset=Course.objects.all()

    def updateCourse(self, serializer,pk):
        course=Course.objects.get(id=pk)
        tutor=Tutor.objects.get(User_Ref=self.request.user)
        if str(course.Author)==str(tutor.User_Ref):
            course.Name=serializer.data['Name']
            course.Desc=serializer.data['Desc']
            course.Author=tutor

            
            tags=serializer.data['Tag_ID']
            

            for tag  in tags:
                course.add(tag)
            course.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
#Update Video API
class UpdateVideo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[Permit1]
    authentication_classes=[TokenAuthentication]
    serializer_class=VideoEditSerializer
    queryset=Video.objects.all()

    def updateVideo(self, serializer,pk):
        video=Video.objects.get(id=pk)
        tutor=Tutor.objects.get(User_Ref=self.request.user)
        if str(video.Author)==str(tutor.User_Ref):
            video.Name=serializer.data['Name']
            video.Desc=serializer.data['Desc']
            video.Author=tutor
            video.Video_Link=serializer.data['Video_Link']
            course1=serializer.data['Course_ID']
            course=Course.objects.get(id=course1)
            video.Course_ID=course
            video.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#Course Enroll API

    


            
            
            




            
            

        
        




        





        
    









        

