from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Student,Teacher
from .forms import StudentProfileForm,TeacherProfileForm,UploadResourceForm
from django.contrib import messages 
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
                p.Teacher=request.user
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
    return render(request,'resource_portal/resource.html')

def books(request):
    return render(request,'resource_portal/books.html')

def teachers(request):
    return render(request,'resource_portal/byteacher.html')

def saved(request):
    return render(request,'resource_portal/saved.html')
