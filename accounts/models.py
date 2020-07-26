from django.db import models
from django.conf import settings
# Create your models here.

class Student(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher.username