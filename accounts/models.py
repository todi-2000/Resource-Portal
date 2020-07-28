from django.db import models
from django.conf import settings
# Create your models here.

Branch = [('None', 'None'),
            ('CS', 'Computer Science and Engineering'),
            ('IT', 'Information Technology'),
             ('EC', 'Electronics and Communication Engineering'),
             ('ME', 'Mechanical Engineering'),
             ('EEE', 'Electrical & Electronics Engineering'),
             ('EE', 'Electrical Engineering'),
             ('CE', 'Civil Engineering'),
]

Year=[
    ('None','None'),
    ('1st','1st Year'),
    ('2nd','2nd Year'),
    ('3rd','3rd Year'),
    ('4th','4th Year'),
]

class Student(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=100,blank=True, null=True)
    college=models.CharField(max_length=200,blank=True, null=True)
    department=models.CharField(max_length=100,choices=Branch,default='None')
    year=models.CharField(max_length=15,choices=Year,default='None')

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=100,blank=True, null=True)
    college=models.CharField(max_length=200,blank=True, null=True)
    department=models.CharField(max_length=500,choices=Branch,default='None')

    def __str__(self):
        return self.teacher.username