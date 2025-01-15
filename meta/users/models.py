from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=150,null=True,blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    short_intro=models.TextField(max_length=500,null=True,blank=True)
    bio=models.TextField(max_length=500,null=True,blank=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return str(self.user)



class Skills(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=250,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


