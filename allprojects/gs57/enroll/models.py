from django.db import models

# Create your models here.

tech_skills = [("python","python"),("react","react"),("java","java"),("javascript","javascript")]

class User(models.Model):
    name = models.CharField(max_length = 70)
    email = models.EmailField()
    password = models.CharField(max_length = 70)
    skill = models.CharField(choices = tech_skills, max_length=50)



