from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView, RedirectView

# template view

# class TemplateClassView(TemplateView):
#     template_name = "school/home.html"

#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         context["name"] = "jiyaulla"
#         context["roll"] = "101"
#         # context = {"name":"ayesha", "roll":102}
#         return context


###############  Templateredirect view

class RedirectClassView(RedirectView):
    url = "https://www.geekyshows.com"

class GeekTempClassView(TemplateView):
    template_name = "school/index.html" 
    