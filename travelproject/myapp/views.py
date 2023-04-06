from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pword = request.POST['password']

        user=auth.authenticate(username=uname,password=pword)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        usrnm=request.POST['username']
        f_name=request.POST['firstname']
        l_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['cpassword']
        if password1==password2:
            if User.objects.filter(username=usrnm).exists():
                messages.info(request,"Username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=usrnm,first_name=f_name,last_name=l_name,email=email,password=password1)
                user.save()
                return redirect('login')
            messages.info(request, "User created")
        else:
            messages.info(request, "Password is not matching")
            return redirect('register')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')