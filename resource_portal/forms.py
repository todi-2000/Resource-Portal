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
        fields=['subject','topic','author','year','type','department','file','thumbnail']
        labels={'subject':'subject','topic':'topic','author':'author','year':'year','type':'type','department': 'department','file':'file','thumbnail':'thumbnail'}
        widgets = {
        'department': forms.Select(attrs={'class':'uSec'}),
        'type': forms.Select(attrs={'class':'uSec'}),
        }
    def __init__(self, *args, **kwargs):
        super(UploadResourceForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'placeholder': 'Subject','class':'uInp'})
        self.fields['topic'].widget.attrs.update({'placeholder': 'Topic','class':'uInp'})
        self.fields['author'].widget.attrs.update({'placeholder': 'Author','class':'uInp'})
        self.fields['year'].widget.attrs.update({'placeholder': 'Year','class':'uInp'})