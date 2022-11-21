from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "enroll/home.html")


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "SUCCESS Congratulations ! Your account is Create")
            messages.add_message(request, messages.INFO, "INFO Congratulations ! Your account is Create")
            messages.add_message(request, messages.WARNING, "WARNING Congratulations ! Your account is Create")
            messages.add_message(request, messages.ERROR, "ERROR Congratulations ! Your account is Create")
#short cut
            messages.success(request, "SUCCESS your account is Created")            
            messages.info(request, "INFO your account is Created")
            messages.warning(request, "WARNING your account is Created")
            messages.error(request, "ERROR your account is Created")            
    else:
        form = UserForm()
    return render(request, "enroll/user.html", {"form":form})