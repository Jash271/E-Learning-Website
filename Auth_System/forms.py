from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    class Meta:
        first_name=forms.CharField(max_length=100)
        last_name=forms.CharField(max_length=100)
        email=forms.EmailField()
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def save(self,commit=True):
        User=super(UserRegistrationForm,self).save(commit=False)
        User.first_name=self.cleaned_data['first_name']
        User.last_name=self.cleaned_data['last_name']
        User.email=self.cleaned_data['email']

        if commit:
            User.save()