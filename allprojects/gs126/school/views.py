from django.shortcuts import render
from school.forms import ContactForm
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django import forms


from school.models import Student
# Create your views here.



# class ContactFormView(FormView):
#     template_name = "school/contact.html"
#     form_class = ContactForm
#     success_url = "/thankyou/"
#     initial = {"name":"jiya", "email":"jiya@gmail.com", "msg":"this is message"}

#     def form_valid(self, form):
#         print(form)
#         s_name = form.cleaned_data["name"]
#         s_email = form.cleaned_data["email"]
#         s_msg = form.cleaned_data["msg"]
#         print("-------------", s_name, s_email, s_msg)
#         return super().form_valid(form)


# 
class ThankyouTemplateView(TemplateView):
    template_name = "school/thankyou.html"



class StudentCreateView(CreateView):
    model = Student
    fields = ["name", "email", "password"]
    success_url = "/stucreate/"
    # success_url = "/thankyou/"

    def get_form(self):
        form = super().get_form()
        form.fields["password"].widget = forms.PasswordInput(attrs={"class":"mypassword"})
        return form



class StudentUpdateView(UpdateView):
    model = Student
    fields = ["name", "email", "password"]
    success_url = "/thankyou/"

    def get_form(self):
        form = super().get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "yourclass"})
        form.fields["password"].widget = forms.PasswordInput(attrs={"class": "yourclass"})
        return form




class StudentDeleteView(DeleteView):
    model = Student
    success_url = "/stucreate/"






# from .forms import StudentForm

# class StudentCreateView(CreateView):
#     form_class = StudentForm
#     template_name = "school/student_form.html"



# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = "school/student_form.html"
#     success_url = "/thankyou/"





