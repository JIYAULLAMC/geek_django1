from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def course_django(request):
    return HttpResponse("this is course django")

def course_python(request):
    return HttpResponse("this is course python")
