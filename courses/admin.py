from django.contrib import admin
from . models import Course,Tag,Tutor,Practice,Submission,Article,Video
# Register your models here.
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Tutor)
admin.site.register(Practice)
admin.site.register(Submission)
admin.site.register(Article)
admin.site.register(Video)