from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project # choose to which model the form should be applied
        fields = ['title','featured_image','description','demo_link','source_link','tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control'
            }),
            'description':forms.Textarea(attrs={
                'class':'input'
            }),
            'title':forms.TextInput(attrs={
                'class':'input'
            }),
            'featured_image':forms.FileInput(attrs={
                'class':'input'
            }),
            'demo_link':forms.TextInput(attrs={
                'class':'input'
            }),
            'source_link': forms.TextInput(attrs={
                'class':'input'
            })
        }

    # def __init__(self,*args,**kwargs):
    #     super(ProjectForm,self).__init__(*args,**kwargs)
    #
    #     self.fields['title'].widget.attrs.update({'class':'input'})


