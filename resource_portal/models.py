from django.db import models
from django.contrib.auth.models import User
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

Type=[
    ('Select','Select'),
    ('Notes','Notes'),
    ('Books','Books'),
    ('Question Papers','Question Papers'),
]

class Resource(models.Model):
    Teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.CharField(max_length=100)
    year=models.CharField(max_length=10,choices=Year,default='None')
    type=models.CharField(max_length=100,choices=Type,default='Select')
    department=models.CharField(max_length=100,choices=Branch,default='None')
    file=models.FileField(upload_to="Files/")
    thumbnail=models.ImageField(upload_to="thumbnail/")

    def __str__(self):
        return self.subject