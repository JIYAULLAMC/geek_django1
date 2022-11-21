from django.shortcuts import render

# Create your views here.


from django.views.generic.list import ListView

from .models import Student

class StudentListView(ListView):
    model = Student

#custom List vie

# class CustomStudentListView(ListView):
#     model = Student
#     template_name_suffix = "_list"  #default
#     template_name_suffix = "_all"  #custom
#     # ordering = "name"
#     ordering = ["name","course"]

# more custome

class CustomStudentListView(ListView):
    model = Student
    template_name = "school/students.html"
    context_object_name = "students"


    def get_queryset(self):
        return Student.objects.filter(course="java")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["datas"] = Student.objects.all().order_by("name")
        return context

    def get_template_names(self):
        if self.request.COOKIES["user"] != "sonam":
            template_name = "school/sonam.html"

        else:
            template_name = self.template_name
        return template_name


################################## detail view 

from django.views.generic.detail import DetailView



# class StudentDetailView(DetailView):
#     model = Student



# class StudentDetailView(DetailView):
#     model = Student
#     template_name = "school/mystudent.html"
#     context_object_name = "stu"
#     #to change the anything insted pk
#     pk_url_kwarg = "mamata"



class MyStudentListView(ListView):
    model = Student
    template_name = "school/allstudent.html"
    context_object_name = "mystudents"


class StudentDetailView(DetailView):
    model = Student
    template_name = "school/mystudent.html"

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["all_data"] = self.model.objects.all()
        return context
   









