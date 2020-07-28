from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Student,Teacher
# Create your views here.
@login_required(login_url='login')
def home(request):
    try:
        user=Student.objects.get(student=request.user)
        context={
            'details':user
        }
    except Student.DoesNotExist:
        user=Teacher.objects.get(teacher=request.user)
        context={
            'details':user
        }
    return render(request,'resource_portal/account.html',context)