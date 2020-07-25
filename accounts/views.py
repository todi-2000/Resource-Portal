from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Student,Teacher
# Create your views here.

def signup(request):
    if request.method=='POST':
        if request.POST['student-username'] is not None:
            susername=request.POST['student-username']
            spassword=request.POST['student-password']
            print(susername)
            try:
                user=User.objects.get(username=susername)
                return redirect('signup')
            except User.DoesNotExist:
                user=User.objects.create_user(username=susername,password=spassword)
                suser=Student.objects.create(student=user)
                suser.save()
                auth.login(request,user)
                return redirect('home')
        if request.POST['teacher-username'] is not None:
            tusername=request.POST['teacher-username']
            tpassword=request.POST['teacher-password']
            try:
                user=User.objects.get(username=tusername)
                return redirect('signup')
            except User.DoesNotExist:
                user=User.objects.create_user(username=tusername,password=tpassword)
                tuser=Teacher.objects.create(teacher=user)
                tuser.save()
                auth.login(request,user)
                return redirect('Home')
    return render(request,'accounts/index.html')

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'accounts/login.html')


def logout(request):
    if request.user:
        auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'accounts/home.html')