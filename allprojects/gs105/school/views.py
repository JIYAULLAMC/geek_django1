from django.shortcuts import render
from .models import Student

from school.managers import CustomManager
# Create your views here.



def home(request): 
    # students =  Student.objects.all()
    students =  Student.students.get_stu_roll_range(10,14)
    return render(request, "school/home.html", {"students":students})