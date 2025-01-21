from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,authenticate,logout
from .forms import LoginForm,RegisterForm,ProfileForm, SkillForm
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
            user=form.save(commit=False)
            user.username = user.username.lower()
            user=form.save()

            messages.success(request, 'Registration completed')
            return redirect('edit-account')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('login')

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


@login_required(login_url='login')
def editAccount(request):

    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request,'users/profile_form.html',context)


@login_required(login_url='login')
def createSkills(request):
    profile=request.user.profile # TODO assossiates the skill with the profile, gives the skill to the requested profile
    form = SkillForm()
    if request.method == 'POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill has been added successfully!')
            return redirect('account')
    context = {'form':form}
    return render(request,'users/skill_form.html',context)


@login_required(login_url='login')
def updateSkills(request,pk):
    profile=request.user.profile # TODO associates the skill with the profile, gives the skill to the requested profile
    skill = profile.skills_set.get(pk=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form=SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill has been updated! ')
            return redirect('account')
    context = {'form':form}
    return render(request,'users/skill_form.html',context)

@login_required(login_url='login')
def deleteSkills(request,pk):
    profile= request.user.profile
    skill = profile.skills_set.get(pk=pk)
    if request.method=='POST':
        skill.delete()
        messages.success(request, 'Skill has been deleted! ')
        return redirect('account')
    context = {'skill':skill}
    return render(request,'users/delete_skill.html',context)