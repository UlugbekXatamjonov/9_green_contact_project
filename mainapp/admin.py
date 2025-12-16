from django.contrib import admin

# Register your models here.

from .models import Check_in

@admin.register(Check_in)
class Check_in_Admin(admin.ModelAdmin):
    list_display  = ("full_name", "school", "grade", "created_on")
    list_filter = ('school', 'grade', "created_on")
    search_fields = ("full_name", 'school', "phone_number")


