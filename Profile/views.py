from django.shortcuts import render
from . forms import ProfileUpdateForm,UserUpdateForm
import pdb
# Create your views here.
def Profile_view(request):
    return render (request,"profile.html")

def update(request):
    if request.method=='POST':
        
    
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return render(request,"profile.html")
    else:
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        

    return render(request,"edit_profile.html",{'u_form':u_form,'p_form':p_form})

def courses(request):
    return render(request,"course_list.html")



