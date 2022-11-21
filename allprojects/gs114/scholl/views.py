from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def myfuncview(request):
    return HttpResponse("<h1>This function base view </h1>")

from django.views import View

class myclassview(View):
    name = "Mamata"

    def get(self, request):
        # return HttpResponse("<h1>This is class base view -GET ")
        # return HttpResponse(self.name)
        return HttpResponse(f"<h1>This is class base view -GET  {self.name} ")


class mychildclassview(myclassview):
    def get(self, request):
        print("----------------------------------")
        return HttpResponse(f"<h1>This is Child class base view -GET  {self.name} ")


class templateclassview(View):
    def get(self, request):
        context = {"msg":"this is class base view CONTEXT"}
        return render(request, "scholl/home.html", context)
    

from .forms import ContactForm

class postclassview(View):
    def get(self, request):
        form = ContactForm()
        return render(request,"scholl/contact.html",{"form":form})


    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print("-----------")
            print(form.cleaned_data["name"])
            print(form.cleaned_data["age"])
        return HttpResponse("form is submitted !")




def news(request, template_name):
    print(template_name)
    return render(request, template_name)



class classmulltemplateview(View):
    #default template we can give empty also
    template_name =  ""
    def get(self, request):
        print(self.template_name, "-----------------------------")
        return render(request, self.template_name)