from django import forms
from django.contrib.auth.models import User
from blog_app.models import Userprofile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')



class UserprofileForm(forms.ModelForm):
