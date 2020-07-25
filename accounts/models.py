from django.db import models
from django.conf import settings
# Create your models here.

class Student(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Teacher(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)