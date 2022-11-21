from django.urls import path
from registration import views
from django.contrib.auth.decorators import login_required


from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    # path("profile/", views.profile, name="profile"),
    # path("about/", views.about, name="about"),
    # class base 
    
    # path("profile/", views.profile.as_view(), name="profile"),
    # path("about/", views.about, name="about"),

    # decorator  in url 

    # path("profile/", login_required(views.profile.as_view()), name="profile"),
    # # path("about/",  login_required(views.about.as_view()), name="about"),
    # path("about/",  staff_member_required(views.about.as_view()), name="about"),

    #deoorating in class
    path("profile/", views.profile.as_view(), name="profile"),
    path("about/", views.about.as_view(), name="about"),
]