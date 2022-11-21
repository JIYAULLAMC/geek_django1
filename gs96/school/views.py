from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Q
from datetime import date, time
# Create your views here.


def home(request):
    students = Student.objects.values_list( "name" ,named=True)
    teachers = Teacher.objects.values_list( "name" ,named=True)
    # students = students.union(teachers)
    # students = students.intersection(teachers)
    # students = students.difference(teachers)

    #operators 

    students = Student.objects.filter(id=6)  |  Student.objects.filter(roll=101)  

    print("+++++++++++++++++++++++++++++++")
    print(students)
    print("=====================================")
    print(students.query)



    return render(request, "school/home.html",{"students": students})


def techerlist(request):
    teachers = Teacher.objects.all()
    return render(request, "school/showdata.html",{"teachers": teachers})
    



















# def home(request):
#     student_data = Student.objects.all()
#     # student_data = Student.objects.filter(marks=98)1
#     # student_data = Student.objects.exclude(marks=98)
#     # student_data = Student.objects.exclude(city="bengaluru")
#     # student_data = Student.objects.exclude(city="-bengaluru")   
#     # student_data = Student.objects.order_by("id").reverse()[: 4]

#     # student_data = Student.objects.values()
#     # student_data = Student.objects.values("name")
#     # student_data = Student.objects.values_list()
#     # student_data = Student.objects.values_list(named=True)
#     # student_data = Student.objects.using('default')


#     #---------------------------------------

#     # print(student_data)
#     # if isinstance(student_data, django.db.models.query.QuerySet):
#     #     print("Yes------------------")
#     #     print(student_data.query)
#     # for student in student_data:
#     #     print(type(student))
#     # qs1 = Student.objects.values_list("id", "name", named=True)
#     # qs2 = Teacher.objects.values_list("id", "name", named=True)
    
#     # student_data = qs2.union(qs1, all=True)

# #
#     # qs1 = Student.objects.values_list("id", named=True)
#     # qs2 = Teacher.objects.values_list("id", named=True)
    
#     # student_data = qs2.intersection(qs1)

#     #difference 
#     # qs1 = Student.objects.values_list("id", "name", named=True)
#     # qs2 = Teacher.objects.values_list("id", "name", named=True)
#     # student_data = qs1.difference(qs2)
 
 
#     # #operators or 
#     # student_data = Student.objects.filter(id=2, roll=102)

#     # student_data = Student.objects.filter(Q(id=2) & Q(roll=102))

#     # #difference 
#     # qs1 = Student.objects.values_list("id", "name", named=True)
#     # qs2 = Teacher.objects.values_list("id", "name", named=True)
#     # student_data = qs1.difference(qs2)
 
 
#     # #operators or 
#     # student_data = Student.objects.filter(id=2, roll=102)

#     # student_data = Student.objects.filter(Q(id=2) | Q(roll=105))

#     #--------------------------------------------------


#     # student_data = Student.objects.in_bulk([1,2])
#     # print(student_data)

#     # student_data = Student.objects.all()
#     # stu_data = Student.objects.get(pk=4)
#     # stu_data1 = Student.objects.get(id=4)
#     # stu_data1.delete()
#     # print("-----------------------",stu_data, stu_data1)

#     # students = Student.objects.filter(marks=95)
#     # students.delete()
#     # print(students)


#     # student_data = Student.objects.all()
#     # # print("-------",student_data.count())
#     # print("-------",student_data.explain())

#     # lookups

#     student_data = Student.objects.all()

#     #exact
#     student_data = Student.objects.filter(name__exact = "vishwa")
#     student_data = Student.objects.filter(name__iexact = "Vishwa")
    
#     #contain
#     student_data = Student.objects.filter(name__contains = "i")
#     student_data = Student.objects.filter(name__icontains = "I")

#     #in

#     student_data = Student.objects.filter(id__in = [1,2,3,4])
#     student_data = Student.objects.filter(marks__in = [98, 90])


#     #greter than

#     student_data = Student.objects.filter(marks__gt=90)
#     student_data = Student.objects.filter(marks__gte=95)

#     # less than

#     student_data = Student.objects.filter(marks__lt= 90)
#     student_data = Student.objects.filter(marks__lte= 90)

#     #starts with


#     student_data = Student.objects.filter(name__startswith = "s")
#     student_data = Student.objects.filter(name__istartswith = "s")

#     #ends with

#     student_data = Student.objects.filter(name__endswith = "a")
#     student_data = Student.objects.filter(name__iendswith = "A")


#     #range

#     student_data = Student.objects.filter(pass_date__range = ("2022-11-05", "2022-11-11"))

#     #date

#     # student_data = Student.objects.filter(pass_date__range = date(2022,11,5))

#     #year
#     student_data = Student.objects.filter(pass_date__year = 2021)

#     student_data = Student.objects.filter(pass_date__month__lte= 10)
#     student_data = Student.objects.filter(pass_date__day__lte= 5)
#     student_data = Student.objects.filter(pass_date__week= 45)
#     student_data = Student.objects.filter(pass_date__quarter= 4)
#     # student_data = Student.objects.filter(pass_date__time__gt= time(6,00))
#     # student_data = Student.objects.filter(pass_date__hour= 5)
#     # student_data = Student.objects.filter(pass_date__minuts=25)
#     # student_data = Student.objects.filter(pass_date__second=25)


#     # aggreegate functions
#     from django.db.models import Avg, Sum, Min, Max, Count

#     student_data = Student.objects.all()
#     average = student_data.aggregate(Avg("marks"))
#     summ = student_data.aggregate(Sum("marks"))
#     minimun = student_data.aggregate(Min("marks"))
#     maximum = student_data.aggregate(Max("marks"))
#     all_count = student_data.aggregate(Count("marks"))


#     print("-----------average", average)
#     print("-----------summ", summ)
#     print("-----------minimun", minimun)
#     print("-----------maximum", maximum)
#     print("-----------all_count", all_count)

#     student_data = Student.objects.filter(roll__isnull = False)



#     # q objects

#     from django.db.models import Q

#     student_data = Student.objects.filter(Q(id=2) & Q(roll=102))
#     student_data = Student.objects.filter(Q(id=2) & Q(roll=107))
#     student_data = Student.objects.filter(Q(id=2) | Q(roll=110))
#     student_data = Student.objects.filter(~Q(id=2))


#     # limition query set 

#     student_data = Student.objects.all()[:5 ]
#     student_data = Student.objects.all()[5:10 ]
#     student_data = Student.objects.all()[1:10:3 ]

#     # print("---------",student_data.query)    
#     return render(request, "school/home.html", { "students" : student_data })