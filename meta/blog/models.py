from django.db import models
import uuid
from users.models import Profile

# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100,default=0,blank=False)
    description= models.TextField(null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True,default='Sking.jpg')
    demo_link=models.CharField(max_length=200,blank=True,null=True)
    source_link=models.CharField(max_length=200,blank=True,null=True)
    tags = models.ManyToManyField('Tag',blank=True) # creates option on admin panel for Project model
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                             primary_key=True,editable=False)


    def __str__(self): #  returns the name of projects on admin panel
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up','up vote'),
        ('down','down vote')
    )
    #owner
    project = models.ForeignKey(Project,on_delete=models.CASCADE) # creates choices for reviews on admin panel
    body = models.TextField(max_length=250,default=0,blank=False) # textfield creates a larger field for inputs rather than charfield
    value=models.CharField(max_length=100,default=0,blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name=models.CharField(max_length=250,default=0,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
