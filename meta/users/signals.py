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


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:  # Check if this is an update, not creation
        if profile.username:  # Ensure username is not None or empty
            user.username = profile.username
        else:
            print("Profile username is missing; keeping the current username.")

        user.first_name = profile.name or user.first_name  # Use existing value if profile.name is None
        user.email = profile.email or user.email  # Use existing value if profile.email is None
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user  # Access the associated user
    if user:  # Check if the user exists
        user.delete()  # Delete the user
        print("Deleting user and profile...")
    else:
        print("No associated user found. Profile deleted.")


post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)