from django.db import models
from django.contrib.auth.models import User
from accounts.models import *
# Create your models here.
Branch = [('None', 'None'),
            ('Computer Science and Engineering', 'Computer Science and Engineering'),
            ('Information Technology', 'Information Technology'),
             ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
             ('Mechanical Engineering', 'Mechanical Engineering'),
             ('Electrical & Electronics Engineering', 'Electrical & Electronics Engineering'),
             ('Electrical Engineering', 'Electrical Engineering'),
             ('Civil Engineering', 'Civil Engineering'),
]

Year=[
    ('None','None'),
    ('1st Year','1st Year'),
    ('2nd Year','2nd Year'),
    ('3rd Year','3rd Year'),
    ('4th Year','4th Year'),
]

Type=[
    ('Select','Select'),
    ('Notes','Notes'),
    ('Books','Books'),
    ('Question Papers','Question Papers'),
]

class Resource(models.Model):
    Teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.CharField(max_length=100)
    topic=models.CharField(max_length=100,blank=True, null=True)
    author=models.CharField(max_length=100,blank=True, null=True)
    year=models.CharField(max_length=10,choices=Year,default='None')
    type=models.CharField(max_length=100,choices=Type,default='Select')
    department=models.CharField(max_length=100,choices=Branch,default='None')
    file=models.FileField(upload_to="Files/")
    thumbnail=models.ImageField(upload_to="thumbnail/")
    favourite=models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.subject