from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.


def projects(request):

    projects = Project.objects.all()
    context={'projects':projects}
    return render(request,'blog/projects.html',context)

def project(request,pk):
    project = Project.objects.get(pk=pk)
    tags = project.tags.all() # gets tags from each project which were taken from the above code
    context = {
        'project':project,
        'tags':tags
    }
    return render(request,'blog/single-projects.html',context)


def createProject(request):
    form = ProjectForm() # form - variable name for the form, ProjectForm - name of form which was created in forms.py
    if request.method =='POST':# saves the posted data
        form = ProjectForm(request.POST,request.FILES)# saves the posted data
        if form.is_valid():# confirms if the form is valid
            form.save() # saves the form
            return redirect('projects') # return users to pages after submitting the form
    context = {'form':form}
    return render(request,'blog/project_form.html',context)


def updateProject(request,pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project) # matches the function with the model form

    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)# matches the function with the model form
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'project':project,'form':form}
    return render(request,'blog/project_form.html',context)


def deleteProject(request,pk):
    project = Project.objects.get(pk=pk)
    context = {'project':project}
    if request.method=='POST':
        project.delete()# deletes the object. We dont need to save it
        return redirect('projects')
    return render(request,'blog/delete_object.html',context)