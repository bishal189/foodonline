from django.contrib import admin
from .models import UserManager,User,Userprofile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# //to maeke admin pannel password uneditable
class customerAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','role','is_active')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(User,customerAdmin)
admin.site.register(Userprofile)