from django import forms
from django.contrib.auth.models import User
from redapp.models import UserProfileInfo
from redapp.models import ViewImage
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        help_texts = {
            'username': None,
            }
        fields=('username','email','password')
class UserProfileInfoForms(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields=('destination','location','phone')
class ViewImageForms(forms.ModelForm):
    class Meta():
        model=ViewImage
        #UserProfileInfo = class defined in models
        #fields contains its attribute
        fields=('profile_pics',)
