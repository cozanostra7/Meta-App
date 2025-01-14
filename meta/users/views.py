from django.shortcuts import render
from .models import *

# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()

    context= {
        'profiles':profiles,

    }
    return render(request,'users/profiles.html',context)


def getProfile(request,pk):
    profile = Profile.objects.get(pk=pk)
    topSKills= profile.skills_set.exclude(description__exact='')
    otherSkills= profile.skills_set.filter(description='')

    context={
        'profile':profile,
        'topSkills':topSKills,
        'otherSkills':otherSkills

    }
    return render(request,'users/user-profile.html',context)