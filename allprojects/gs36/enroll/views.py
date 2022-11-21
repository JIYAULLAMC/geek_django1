from django.shortcuts import render
# from enroll.models import Student
from enroll.forms import Register
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def stuinfo(request):
    # stus = Student.objects.all()  
    return render(request, "enroll/home.html")

# def showform(request):   
#     if request.method == "POST":
#         form_data = Register(request.POST)        
#         if form_data.is_valid():
#             form = form_data
#             form.save()
#             return HttpResponseRedirect("regi/home/")
#             # return render(request, "enrolL/home.html", {'form': form})
#     else:
#         form = Register()
#     return render(request, "enroll/registerpage.html", {'form': form})


def showform(request):   
    if request.method == "POST":
        form = Register(request.POST)        
        if form.is_valid():
            name  = form.cleaned_data['name']
            password1  = form.cleaned_data['password1']
            password2  = form.cleaned_data['password2']
            print("--------------name", name)
            print("--------------password1", password1)
            print("--------------password2", password2)
    else:
        form = Register()
    return render(request, "enroll/registerpage.html", {'form': form})