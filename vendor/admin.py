from django.contrib import admin
from .models import vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display=('user','vendor_name','is_approved','created_at')
    list_display_links=('user','vendor_name',)
    list_editable=('is_approved',)

admin.site.register(vendor,VendorAdmin)