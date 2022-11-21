from django.db import models

from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)



class Singer(models.Model):
    singer = models.CharField(max_length= 50)
    age = models.IntegerField()

    def my_singer(self):
        print(self.__dict__)

        return self.singer

class Song(models.Model):
    song = models.CharField(max_length=100)
    duration = models.IntegerField()
    singer = models.ManyToManyField(Singer)
