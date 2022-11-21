from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic import TemplateView
# Create your views here.


# @login_required
# def profile(request):
#     return render(request, "registration/profile.html")

# @staff_member_required
# def about(request):
#     return render(request, "registration/about.html")


#to work withe the url decorators in urlfile for 


# class profile(TemplateView):
#     template_name = "registration/profile.html"

# class about(TemplateView):
#     template_name = "registration/about.html"



from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# class profile(TemplateView):
#     template_name = "registration/profile.html"

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)



# class about(TemplateView):
#     template_name = "registration/about.html"

#     @method_decorator(staff_member_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)


################################################################################




@method_decorator(login_required, name="dispatch")
class profile(TemplateView):
    template_name = "registration/profile.html"

   



@method_decorator(staff_member_required, name="dispatch")
class about(TemplateView):
    template_name = "registration/about.html"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



