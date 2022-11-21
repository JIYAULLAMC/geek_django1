from django.shortcuts import render
# Create your views here.


#abstract class

# from .models import Student, Teacher, Constructor
# def home(request):
#     students = Student.objects.all()
#     teachers = Teacher.objects.all()
#     constructors = Constructor.objects.all()
#     return render(request, "school/home.html", {"students":students,"teachers":teachers,"constructors":constructors})


from .models import ExamCenter, Student

def index(request):
    students = Student.objects.all()
    examcenters = ExamCenter.objects.all()
    return render(request, "school/index.html", {"students":students,"examcenters":examcenters})

