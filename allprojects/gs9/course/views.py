from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def coursedj(request):
#     return HttpResponse("this is course dj")


# def coursepy(request):
#     return HttpResponse("this is course py")

def coursedj(request):
    return render(request, 'course/coursedj.html', status=210)


def coursepy(request):
    return render(request, 'course/coursepy.html', status=205)