from django import forms 
from . models import Profile
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['Bio','Display_Pic','Github_Link']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
