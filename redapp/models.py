from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,help_text=False)
    location=models.CharField(max_length=128)
    destination=models.CharField(max_length=128)
    phone=models.CharField(max_length=128)
class ViewImage(models.Model):
    #portfolio_site=models.URLField(blank=True)
    profile_pics = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
