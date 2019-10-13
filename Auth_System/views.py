from django.shortcuts import render,redirect

from . forms import UserRegistrationForm 
from django.contrib.auth.forms import  UserCreationForm
from django.core.mail import send_mail
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
    return render(request,'home.html')