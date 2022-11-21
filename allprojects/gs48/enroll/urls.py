from django.urls import path
from enroll import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("home/", views.home,{'status': "Good"}, name="home"),
    path("student/<int:id>/",views.show_details, name="detail"),
    path("student/<int:id>/<int:my_id>/",views.show_subdetails, name="sub_detail"),
]