from django.contrib import admin
from school.models import Teacher, Student
# Register your models here.



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "teacher_id", "teacher_firstname", "teacher_lastname", "teacher_salary"]



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "student_id", "student_firstname", "student_lastname", "student_fees", "teacher"]
    actions = ['delete_teacher_method']

    @admin.action(description="Delete Teacher Method")
    def delete_teacher_method(self, request, queryset):
        print("deleter teacher method")
        print("-------------------------------------")
        print(queryset)

        for obj in queryset:
            print("obj------",obj.__dict__)
            print(obj.teacher_id)
            Student.objects.filter(student_id=obj.student_id).update(teacher=None)
            my_obj = Teacher.objects.filter(teacher_id= obj.teacher_id).delete()
            print(my_obj)
