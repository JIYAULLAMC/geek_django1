from django.db import models

# Create your models here.




class Teacher(models.Model):
    teacher_id = models.IntegerField(unique=True)
    teacher_firstname = models.CharField(max_length=20)
    teacher_lastname = models.CharField(max_length=20)
    teacher_salary = models.IntegerField()


    def __str__(self):
        return self.teacher_firstname

    def __unicode__(self):
        return self.id


    

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    student_firstname = models.CharField(max_length=20)
    student_lastname = models.CharField(max_length=20)
    student_fees = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.student_firstname

    def __unicode__(self):
        return self.id





