"""gs116 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # template view 

    # path("",views.TemplateView.as_view(template_name="school/home.html"), name="home"),
    # # path("index/",views.TemplateClassView.as_view(), name="index"),
    # path("index/",views.TemplateClassView.as_view(extra_context = {"course":"Python"}), name="index"),

    ###########  Templateredirect  views
    path("",views.TemplateView.as_view(template_name="school/home.html"), name="base"),
    path("home/",views.RedirectView.as_view(url="/"), name="home"),
    path("index/",views.RedirectView.as_view(url="/"), name="index"),
    #external website
    path("google/",views.RedirectView.as_view(url="https://www.google.com"), name="google"),
    # we wont mentionin as_view()
    path("geeky/",views.RedirectClassView.as_view(), name="geeky"),


    #using pattern  
    path("myindex/",views.RedirectView.as_view(pattern_name="base"), name="myindex"),
    path("tohome/",views.RedirectView.as_view(pattern_name="home"), name="tohome"),
    #ex
    path("seehome/",views.RedirectView.as_view(url="something/"), name="seehome"),
    path("toohome/",views.RedirectView.as_view(pattern_name="seehome"), name="toohome"),

    #rendering one to another template 
    path("geekhome/<int:pk>/",views.RedirectView.as_view(pattern_name="to-geek"), name="geekhome"),
    path("<int:pk>/",views.GeekTempClassView.as_view(), name="to-geek"),



    

]
