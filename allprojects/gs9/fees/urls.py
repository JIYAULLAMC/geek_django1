from django.urls import path
from fees import views

urlpatterns = [
    path("feesdj/",views.feesdj),
    path("feespy/",views.feespy),
]