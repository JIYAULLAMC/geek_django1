from django.contrib import admin

# Register your models here.


# from .models import Student, Teacher, Constructor
#abstract class

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "age", "fees"]

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "age","date", "salary"]

# @admin.register(Constructor)
# class ConstructorAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "age", "payment"]



#----------------------------------------
#multi table


from .models import ExamCenter, Student

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ["id", "cname", "city"]



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "cname", "city", "name", "roll"]



