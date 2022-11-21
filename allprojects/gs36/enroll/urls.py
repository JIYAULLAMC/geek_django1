from django.urls import path
from enroll import views

urlpatterns = [
    path("home/",views.stuinfo),
    path("register/",views.showform)
]