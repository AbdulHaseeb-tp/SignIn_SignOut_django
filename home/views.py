from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'You entered a invalid user credentials')
    return render(request, 'signin.html')


def signup(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=User.objects.create_user(username,email,password)
        user.save()
        
        return redirect('signin')

    return render(request, 'signup.html')



def signout(request):
    logout(request)
    return redirect('signin')