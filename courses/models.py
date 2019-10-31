from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutor(models.Model):
    User_Ref=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str(self):
        return self.User_Ref.username




class Tag(models.Model):
    Name=models.TextField()
    Desc=models.TextField()
    def __str__(self):
        return self.Name

class Course(models.Model):
    Name=models.TextField()
    Desc=models.TextField()
    Author=models.ForeignKey(Tutor,on_delete=models.CASCADE)
    Enrollment_ID=models.ManyToManyField(User,blank=True)
    Tag_ID=models.ManyToManyField(Tag)
    Date_of_Publishing=models.DateTimeField(auto_now=True)
    Completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Name

class Video(models.Model):
    Name=models.TextField()
    Video_Link=models.URLField()
    DOP=models.DateTimeField(auto_now=True)
    Desc=models.TextField()
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)
    Author=models.ForeignKey(Tutor,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Practice(models.Model):
    Name=models.TextField()
    Desc=models.TextField()
    Lec_Ref=models.ForeignKey(Video,on_delete=models.CASCADE)
    Author=models.ForeignKey(Tutor,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Submission(models.Model):
    Problem_Ref=models.ForeignKey(Practice,on_delete=models.CASCADE)
    Code=models.FileField()
    Author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __int__(self):
        return self.Problem_Ref

class Article(models.Model):
    Title=models.TextField()
    Ref_Link=models.URLField()
    Tag_ID=models.ManyToManyField(Tag)
    def __str__(self):
        return self.Title








