from django.contrib import admin
from .models import Post, Song, Singer
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ "user", "title", "desc"]
    

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = [ "singer", "age", "my_singer"]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Song._meta.get_fields() if not field.many_to_many]


print([field.name for field in Song._meta.get_fields() if not field.many_to_many])