from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




def fees_django(request):
    return HttpResponse("fees django")

def fees_python(request):
    return HttpResponse("fees python")