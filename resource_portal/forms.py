from django import forms
from accounts.models import Student,Teacher
from .models import Resource

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','college','department','year']
        labels={'name':'Name','email':'Email','college':'College','department': 'Department','year':'Year'}
        widgets = {
        'department': forms.Select(attrs={'class':'uSec'}),
        'year': forms.Select(attrs={'class':'uSec'}),
        }
    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name','class':'uInp'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email','class':'uInp'})
        self.fields['college'].widget.attrs.update({'placeholder': 'Your College','class':'uInp'})

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['name','email','college','department']
        labels={'name':'Name','email':'Email','college':'College','department': 'Department'}
        widgets = {
        'department': forms.Select(attrs={'class':'uSec'}),
        }
    def __init__(self, *args, **kwargs):
        super(TeacherProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name','class':'uInp'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email','class':'uInp'})
        self.fields['college'].widget.attrs.update({'placeholder': 'Your College','class':'uInp'})


class UploadResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields="__all__"