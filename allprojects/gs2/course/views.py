from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def learndj(request):
    return HttpResponse("Learn django")


def learnpy(request):
    return HttpResponse("Learn Python")


def learn_var(request):
    a = "<h1>this is varibale </h1>"
    return HttpResponse(a)


def learn_math(request):
    a = 10+10
    return HttpResponse(a)


def learn_format(request):
    a = "Geeky Shows"
    return HttpResponse(f"Hello {a}")


def index(request):
    return HttpResponse("index page")
