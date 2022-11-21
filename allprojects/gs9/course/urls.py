from django.urls import path
from course import views

urlpatterns = [
    path("coursedj/",views.coursedj),
    path("coursepy/",views.coursepy),
]