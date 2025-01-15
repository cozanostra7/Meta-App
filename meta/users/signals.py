from django.db import models
from django.contrib.auth.models import User
import uuid
from .models import *

#@receiver(post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    print('User saved!')
    if created:
        user=instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()
    print('Deleting user ...')


post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)