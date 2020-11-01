from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Student,Teacher
from .forms import StudentProfileForm,TeacherProfileForm,UploadResourceForm
from django.contrib import messages 
from .models import *
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='login')
def home(request):
    try:
        user=Student.objects.get(student=request.user)
        context={
            'details':user,
            'student':1
        }
    except Student.DoesNotExist:
        user=Teacher.objects.get(teacher=request.user)
        context={
            'details':user,
            'student':0,
        }
    return render(request,'resource_portal/account.html',context)

@login_required(login_url='login')
def ProfileEditForm(request):
    context={}
    try:
        student=Student.objects.get(student=request.user)
        if request.method=='POST':
            form=StudentProfileForm(request.POST,instance=student)
            if form.is_valid():
                user=form.save(commit=False)
                user.student=request.user
                user.save()
                return redirect('home')
        form=StudentProfileForm(instance=student)
        context={
            'form':form,
            'student':1
        }
    except Student.DoesNotExist:
        teacher=Teacher.objects.get(teacher=request.user)
        if request.method=='POST':
            form=TeacherProfileForm(request.POST,instance=teacher)
            if form.is_valid():
                user=form.save(commit=False)
                user.teacher=request.user
                user.save()
                return redirect('home')
        form=TeacherProfileForm(instance=teacher)
        context={
            'form':form,
            'student':0
        }
    return render(request,'resource_portal/profileform.html',context)

@login_required(login_url='login')
def uploadresources(request):
    try:
        user=Teacher.objects.get(teacher=request.user)
        if request.method=="POST":
            form=UploadResourceForm(request.POST,request.FILES)
            if form.is_valid():
                p=form.save(commit=False)
                p.Teacher=Teacher.objects.get(teacher=request.user)
                p.save()
                messages.success(request, 'Uploaded Successfully!')
                return redirect('home')
        form=UploadResourceForm()
        context={
            'form':form
        }
        return render(request,'resource_portal/resUp.html',context)
    except Teacher.DoesNotExist:
        return redirect('home')

def index(request):
    return render(request,"resource_portal/index.html")

def resources(request):
    context={
        'resources':Resource.objects.all()
    }
    return render(request,'resource_portal/resource.html',context)

def books(request):
    context={
        'books':Resource.objects.filter(type="Books")
    }
    return render(request,'resource_portal/books.html',context)

def teachers(request):
    resources=Resource.objects.all()
    teachers=[]
    for res in resources:
        if res.Teacher!=None:
            teachers.append(res)
    print(teachers)
    context={
        'teacher':teachers
    }
    return render(request,'resource_portal/byteacher.html',context)

def saved(request):
    return render(request,'resource_portal/saved.html')

def deleteresource(request):
    if request.method=="POST" and request.is_ajax:
        print(request.POST)
        val=request.POST['id_num']
        Resource.objects.get(id=int(val)).delete()
        return HttpResponse(val)
    user=Teacher.objects.get(teacher=request.user)
    resources=Resource.objects.filter(Teacher=user)
    context={
        'resource':resources
    }
    return render(request,'resource_portal/delete.html',context)
    
