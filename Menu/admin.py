from django.contrib import admin
from .models import *

# Register your models here.

class categoryadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','vendor','updated_at')
    search_fields=('category_name','vendor__vendor_name')



class fooditemadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('food_title',)}
    list_display=('food_title','Category','vendor','price','is_availabe','updated_at')
    search_fields=('food_title','Category__category_name','vendor__vendor_name')
    list_filter=('is_availabe',)
admin.site.register(Category,categoryadmin)
admin.site.register(Fooditem,fooditemadmin)