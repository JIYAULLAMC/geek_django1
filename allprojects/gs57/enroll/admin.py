from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password","skill"]
    list_filter = ["name", ("email", admin.EmptyFieldListFilter)]
    # radio_fields = {"skill": admin.HORIZONTAL}
    search_fields= ['skill',]
    # save_on_top = True
    # list_per_page = 2
    list_max_show_all = 2
    # list_editable = ("name",)
    # save_as = True
    # inlines = ["id","name"]
    actions_on_bottom = True


