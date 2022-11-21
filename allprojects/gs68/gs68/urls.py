"""gs68 URL Configuration

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
from student import views

urlpatterns = [
    path("admin/", admin.site.urls),

# createing and storing and destroyiing the cookies
    path("setcookie/", views.setcookie, name="usetcookie"),
    path("getcookie/", views.getcookie, name="ugetcookie"),
    path("delcookie/", views.delcookie, name="udelcookie"),

# createing and storing and destroyiing the sessions
    path("setsession/", views.setsession, name="usetsession"),
    path("getsession/", views.getsession, name="ugetsession"),
    path("delsession/", views.delsession, name="udelsession"),
    
# checking test cookies
    path("settestcookie/", views.settestcookie, name="settestcookie"),
    path("checktestcookie/", views.checktestcookie, name="checktestcookie"),
    path("deltestcookie/", views.deltestcookie, name="deltestcookie"),
]
