from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
 
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    Bio=models.TextField()
    Display_Pic=models.ImageField(default='default.jpg',upload_to='profile_images')
    Github_Link=models.URLField()

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)


