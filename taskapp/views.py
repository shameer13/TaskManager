from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from taskapp.models import Task


# Create your views here.
def home(request):
    data = {"login":True,"sign":True}
    return render(request,'signin.html',data)


def login_fun(request):
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["pswd"]
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return render(request,'dashboard.html')
        else:
            # data = {"msg": True}
            data = {"login": True, "sign": False}
            return render(request,'signin.html', data)
    else:
        # data = {"msg": True}
        data = {"login": True, "sign": False}
        return render(request, 'signin.html', data)



    return render(request,'login.html')


def signin_fun(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtemail"]
        password=request.POST["txtpswd"]
        if User.objects.filter(Q(username=name)|Q(email=email)|Q(password=password)).exists():
            data = {"login": False, "sign": True}
            return render(request,'signin.html')
        else:
            u1=User.objects.create_superuser(username=name,email=email,password=password)
            u1.save()
            data = {"login": True, "sign": False}
            return render(request,'signin.html',data)
    data = {"login": False, "sign": True}
    return render(request,'signin.html')


def display_fun(request):
    data = Task.objects.all()
    return render(request,'dashboard.html',{"tasks":data,"display":True})