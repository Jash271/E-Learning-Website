from . models import Course,Tutor,Tag,Video,Practice
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import  serializers
from django.contrib.auth.models import User
from requests.api import request



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['Name','Desc']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

class TutorSerializer(serializers.ModelSerializer):
    User_Ref=UserSerializer(many=False,read_only=True)
    class Meta:
        model=Tutor
        fields=['User_Ref']



class CourseSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['Name','Desc','Tag_ID',]
    

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Video
        fields=['Name','Desc','Video_Link']
        
class CourseSerializer3(serializers.ModelSerializer):
    videos=serializers.StringRelatedField(many=True)
    class Meta:
        model=Course
        fields=['Name','Desc','Tag_ID','videos']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    



class TutorSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model=Tutor
        fields=['User_Ref']



class VideoEditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Video
        fields=['Name','Desc','Video_Link','Course_ID']

class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']
    

class TutorSerializer1(serializers.ModelSerializer):
    User_Ref=UserSerializer1(many=False,read_only=True)
    class Meta:
        model=Tutor
        fields=['User_Ref']

class CourseSerializer(serializers.ModelSerializer):
    Tag_ID = TagSerializer(many=True, read_only=True)
    Author=TutorSerializer1(many=False,read_only=True)
    videos=VideoSerializer(many=True,read_only=True)
    
    class Meta:
        model=Course
        fields=['Name','Desc','Author','Tag_ID','Date_of_Publishing','videos']
        
class Practiceserializer(serializers.ModelSerializer):
    class Meta:
        model=Practice
        fields=['Name','Desc','Lec_Ref']


class CourseSerializer4(serializers.ModelSerializer):
    
    class Meta:
        model=Course
        fields=['Name','Desc','Tag_ID']