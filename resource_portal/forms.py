from django import forms
from accounts.models import Student,Teacher

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','college','department','year']
        labels={'name':'Name','email':'Email','college':'College','department': 'Department','year':'Year'}

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['name','email','college','department']
        labels={'name':'Name','email':'Email','college':'College','department': 'Department'}