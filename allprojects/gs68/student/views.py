from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# createing and storing and destroyiing the cookies

def setcookie(request):
    response = render(request, "student/setcookie.html")
    response.set_cookie("name","jiyaulla", max_age=15)
    return response


def getcookie(request):
    # mycookie = request.COOKIES["name"]
    mycookie = request.COOKIES.get("name", "no data")
    print("----------------",mycookie)
    return render(request, "student/getcookie.html",{"my":mycookie})

def delcookie(request):
    response = render(request, "student/delcookie.html")
    response.delete_cookie("name")
    return response

# def setsession(request):
#     request.session["name"] = "Mamata"
#     request.session["lname"] = "jiya"
#     request.session.set_expiry(3)
#     return render(request, "student/setsession.html")

# def getsession(request):
#     # name = request.session["name"]
#     name = request.session.get("name", default = "no data")


#     if "name" in  request.session:
#         name = request.session['name']
#         request.session.modified = True
#         return render(request, "student/getsession.html", {"name":name})
#     else:
#         return HttpResponse("Your session is expired!")
#     # print("----------",name)
#     # print(request.session.get_session_cookie_age())
#     # print(request.session.get_expiry_age())
#     # print(request.session.get_expiry_date())
#     # print(request.session.get_expire_at_browser_close())
#     # for key in request.session.keys() :
#         # print("---------", key)
#     # for value in request.session.values() :
#         # print("---------", value)
#     # for item in request.session.items() :
#     #     print("---------", item)
#     # return render(request, "student/getsession.html",{"name":name, })

# def delsession(request):
#     # if "name" in request.session:
#     #     del request.session["name"]
#     request.session.flush()
#     request.session.clear_expired()
#     return render(request, "student/delsession.html")




# test cookie wherther the browser will suport or not 




def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, "student/settestcookie.html")


def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, "student/checktestcookie.html")



def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, "student/deltestcookie.html")




# how to store the session in file

def setsession(request):
    request.session["name"] = "Mamata Mohammed Chindadi"
    return render(request, "student/setsession.html")

def getsession(request):
    name = request.session.get("name", default = "no data")
    if "name" in  request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, "student/getsession.html", {"name":name})
    else:
        return HttpResponse("Your session is expired!")
  

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, "student/delsession.html")


