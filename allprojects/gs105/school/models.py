from django.db import models

# Create your models here.

from school.managers import CustomManager

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    
    mymanager = models.Manager()
    students = CustomManager()
    objects = models.Manager()


