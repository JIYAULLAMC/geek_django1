from django.contrib import admin

# Register your models here.

from student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "firstname", "lastname",]