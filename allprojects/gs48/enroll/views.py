from django.shortcuts import render
from enroll.forms import UserForm

# Create your views here.



def register(request):
    print("***********************************")
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            print("-------", nm, em, pwd)
    else : 
        fm = UserForm()
    return render(request, "enroll/register.html", {"form":fm})




def home(request,status):
    print(status)
    return render(request, "enroll/home.html", {"status": status})

# def show_details(request, my_id):
#     print("------------------------------------")
#     print(type(my_id))
#     return render(request, 'enroll/show.html', {"my_id":my_id})

def show_details(request, id):
    print("------------------------------------")
    if id==1:
        student = {"id":1, "name":"aaaaa"}
    if id==2:
        student = {"id":2, "name":"bbbbbb"}
    if id==3:
        student = {"id":3, "name":"ccccc"}
    if id==4:
        student = {"id":4, "name":"dddddd"}

    return render(request, 'enroll/show.html', {"student":student})

def show_subdetails(request, id, my_id):
    print("------------------------------------")
    if id==1 and my_id == 5:
        student = {"id":1, "name":"aaaaa", "sub_id": f"ths is subid{my_id}"}
    if id==2 and my_id == 6:
        student = {"id":2, "name":"bbbbbb", "sub_id": f"ths is subid{my_id}"}
    if id==3 and my_id == 7:
        student = {"id":3, "name":"ccccc", "sub_id": f"ths is subid{my_id}"}
    if id==4 and my_id == 8:
        student = {"id":4, "name":"dddddd", "sub_id": f"ths is subid{my_id}"}

    return render(request, 'enroll/show.html', {"student":student})