
from django.shortcuts import render
from redapp.forms import UserForm
from redapp.forms import UserProfileInfo,UserProfileInfoForms,ViewImageForms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'codist/index.html')
@login_required
def special(request):
    return HttpResponse("you are logged in")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered=False
    if request.method=='POST':
           user_form=UserForm(data=request.POST)
           profile_form=UserProfileInfoForms(data=request.POST)
           image_form=ViewImageForms(data=request.POST)
           if user_form.is_valid() and profile_form.is_valid():
                user=user_form.save()
                user.set_password(user.password)
                user.save()
                profile=profile_form.save(commit=False)
                profile.user=user
                profile.save()
                registered=True
           else:
              print(user_form.errors,profile_form.errors)
    else:
        user_form=  UserForm()
        profile_form= UserProfileInfoForms()
    return render(request,'codist/registration.html',
                 {'user_form':user_form,
                 'profile_form':profile_form,
                 'registered':registered})
@login_required
def image(request):
    image_form=ViewImageForms()
    if 'profile_pics' in request.FILES:
        print('found it')
        profile=image_form.save(commit=False)
        profile.profile_pics=request.FILES['profile_pics']
    return render(request,'codist/upload.html',{'image_form':image_form})
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("not registered")
        else:
            print("someone tried")
            return HttpResponse("invalid")
    else:
        return render(request,'codist/login.html')

# Create your views here.
