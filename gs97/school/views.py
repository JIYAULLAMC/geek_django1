from django.shortcuts import render
from school.models import Teacher, Student
# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpResponse



class home(TemplateView):
    template_name = "school/home.html"



# delete techer of DDDD

def delete(request):
    obj = Teacher.objects.get(id=1)
    print("*******", obj.__dict__)
    return HttpResponse("the data is deleted")


