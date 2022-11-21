from django.urls import path
from fees import views


urlpatterns = [
    path("fd/",views.fees_django),
    path("fp/", views.fees_python),
]