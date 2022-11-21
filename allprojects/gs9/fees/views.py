from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def feesdj(request):
    return render(request, "fees/feesdj.html", status=200)


def feespy(request):
    return render(request, "fees/feespy.html", status=215)


# def feesdj(request):
#     return HttpResponse("this is fees dj")


# def feespy(request):
#     return HttpResponse("this is fees py")