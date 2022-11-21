from django.shortcuts import render
from student.models import Student
from student.forms import StudentForm
# Create your views here.


from django.views.generic.base import TemplateView, RedirectView, View

from django.http import HttpResponse, HttpResponseRedirect
class addshowdata(TemplateView):
    template_name = "student/home.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context = {'students': Student.objects.all(), "form":StudentForm()}
        return context

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/")



class DeleteStudent(RedirectView):
    url="/"
    def get_redirect_url(self, *args,**kwargs):
        stu_del = kwargs['id']
        Student.objects.get(id=stu_del).delete()        
        return super().get_redirect_url(*args, **kwargs)



class UpdateStudent(View):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request, "student/update.html", {"form":form})

    def post(self,request,id):         
        predata = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=predata)
        if form.is_valid():
            form.save()
        return render(request, "student/update.html", {"form":form})

        
        

