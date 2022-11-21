"""gs114 URL Configuration

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
from scholl import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("myfuncview/", views.myfuncview, name="myfuncview"),
    # path("myclassview/", views.myclassview.as_view(), name="myclassview"),
    path("myclassview/", views.myclassview.as_view(name="Mohammed"), name="myclassview"),
    path("mychildclassview/", views.mychildclassview.as_view(), name="mychildclassview"),
    path("templateclassview/", views.templateclassview.as_view(), name="templateclassview"),
    path("postclassview/", views.postclassview.as_view(), name="postclassview"),

    #rendering two templates with one view

    path("news1/", views.news,{"template_name":"scholl/news1.html"}, name="news1"),
    path("news2/", views.news,{"template_name":"scholl/news2.html"}, name="news2"),

    # this is class base mutiple template context view

    path("classmulltemplateview1/", views.classmulltemplateview.as_view(template_name= "scholl/news1.html"), name="classmulltemplateview"),
    path("classmulltemplateview2/", views.classmulltemplateview.as_view(template_name= "scholl/news2.html"), name="classmulltemplateview"),

]
