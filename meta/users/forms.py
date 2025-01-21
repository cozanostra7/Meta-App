from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input'
    }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    username= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','bio',
                  'short_intro','profile_image','social_github']



class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['owner'] # exlcudes the field mentioned in it

    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})