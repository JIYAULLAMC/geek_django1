from django.urls import path
from enroll import views

urlpatterns = [
    path("",views.stuinfo),
    path("registration/",views.showform)
]