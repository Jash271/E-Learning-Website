from django import forms
from . models import Submission
class ContactForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Desc = forms.CharField(widget=forms.Textarea)
    Link = forms.CharField(max_length=100)

class ProblemForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Desc = forms.CharField(max_length=100)

class SolutionForm(forms.Form):
    Code = forms.FileField()
    


