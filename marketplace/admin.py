from django.contrib import admin
from .models import Cart

# Register your models here.
class Cartadmin(admin.ModelAdmin):
    list_display=('user','fooditem','modified_at')
admin.site.register(Cart,Cartadmin)