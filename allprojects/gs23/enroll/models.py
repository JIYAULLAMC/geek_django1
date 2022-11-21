from django.db import models

# Create your models here.


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length= 70)
    stuemail = models.EmailField()
    stupass = models.CharField(max_length= 70)
    
    



    # def __str__(self):
    #     return str(self.stuid)

    def fname(self):
        return self.stuid

