from rest_framework import permissions
from . models import Tutor,Course
from django.contrib.auth.models import User
from requests.api import request


class Permit(permissions.BasePermission):
    message='Access Denied '
    def has_permission(self, request, view):
        try:
            t=Tutor.objects.get(User_Ref=request.user)
            try:
                course=Course.objects.get(Author=t)
                return True
            except:
                return False
            
        except:
            return False
            
class Permit1(permissions.BasePermission):
    message='Access Denied '
    def has_permission(self, request, view):
        try:
            t=Tutor.objects.get(User_Ref=request.user)
            
            return True
            
        except:
            return False

            

            
            
        
       

        

