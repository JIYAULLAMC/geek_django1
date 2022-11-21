from django.urls import path
from course import views

urlpatterns = [
    path("ld/", views.learn_django),
    path("lp/", views.learn_python),
]