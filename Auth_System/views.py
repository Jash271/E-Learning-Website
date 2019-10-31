from django.shortcuts import render,redirect
from courses.models import Tutor
from . forms import UserRegistrationForm 
from django.contrib.auth.forms import  UserCreationForm
from django.core.mail import send_mail
import pdb
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserRegistrationForm()
    return render(request,'registration_form.html',{'form':form})
 

def home(request):
    flag=0
    flag=Tutor.objects.filter(User_Ref=request.user).count()
    
    if (flag>0):
        flag=1
    else:
        flag=0

  
   
    return render(request,'home.html',{'flag':flag})