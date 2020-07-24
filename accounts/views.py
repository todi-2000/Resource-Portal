from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpass=request.POST['confirmpassword']
        if password==confirmpass:
            try:
                user=User.objects.get(username=username)
                return redirect('signup')
            except User.DoesNotExist:
                user=User.objects.create_user(username=username,password=password)
                auth.login(request,user)
                return redirect('Home')
        else:
            return redirect('signup')
    return render(request,'accounts/index.html')

def login(request):
    if request.method=='POST':
        user=User.objects.get(username=request.POST['username'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'accounts/home.html')