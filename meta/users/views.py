from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,authenticate,logout
from .forms import LoginForm,RegisterForm
from django import forms
from django.contrib import messages


from django.contrib.auth.models import User
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            if user:
                login(request,user)
                messages.success(request, 'You are logged in! ')



                return redirect('profiles')
            else:

                messages.error(request, 'You entered wrong email or Username')
                return redirect('login')



    else:

        form=LoginForm()


    context = {
        'form': form,
        'title':'Log in'
    }
    return render(request,'users/user-login.html',context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'You are logged out! ')
    return redirect('login')

def registerUser(request):
    if request.method=='POST':
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Registration completed')
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('register')

    else:
        form=RegisterForm()

    context={
        'form': form
    }
    return render(request,'users/user-register.html',context)

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


@login_required(login_url='login')
def userAccount(request):

    profile=request.user.profile
    skills= profile.skills_set.all()
    projects = profile.project_set.all()

    context= {'profile':profile,
              'skills':skills,
              'projects':projects
              }
    return render(request,'users/account.html',context)
