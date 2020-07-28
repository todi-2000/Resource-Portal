from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import Student,Teacher
# Create your views here.

def signup(request):
    if request.method=='POST':
        try:
            if request.POST['student-username'] is not None:
                susername=request.POST['student-username']
                spassword=request.POST['student-password']
                try:
                    user=User.objects.get(username=susername)
                    return redirect('signup')
                except User.DoesNotExist:
                    user=User.objects.create_user(username=susername,password=spassword)
                    suser=Student.objects.create(student=user)
                    suser.save()
                    auth.login(request,user)
                    return redirect('home')
        except MultiValueDictKeyError:
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
                    return redirect('home')
    return render(request,'accounts/index.html')

def login(request):
    if request.method=='POST':
        if 'student-username' in request.POST:
            user=auth.authenticate(username=request.POST['student-username'],password=request.POST['student-password'])
            if user is not None:
                try:
                    if Student.objects.filter(student=user).exists():
                        auth.login(request,user)
                        return redirect('home')
                except Student.DoesNotExist:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            user=auth.authenticate(username=request.POST['teacher-username'],password=request.POST['teacher-password'])
            if user is not None:
                try:
                    if Teacher.objects.filter(teacher=user).exists():
                        auth.login(request,user)
                        return redirect('home')
                except Teacher.DoesNotExist:
                    return redirect('login')
                
            else:
                return redirect('login')
    return render(request,'accounts/login.html')


def logout(request):
    if request.user:
        auth.logout(request)
    return redirect('login')