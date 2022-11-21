from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "course"]

    