from django.shortcuts import render
from django.shortcuts import get_object_or_404
from vendor.models import vendor
from Menu.models import Category,Fooditem
from django.db.models import Prefetch


# Create your views here.

def marketplace(request):
   Vendor=vendor.objects.filter(is_approved=True,user__is_active=True)
   Vendor_count=Vendor.count()
   context={
      'vendor':Vendor,
      'vendor_count':Vendor_count
   }
   return render(request,'marketplace/listing.html',context)



def vendor_details(request,vendor_slug):
   Vendor=get_object_or_404(vendor,vendor_slug=vendor_slug)
   category=Category.objects.filter(vendor=Vendor).prefetch_related(
    Prefetch(
      'fooditems',
      queryset=Fooditem.objects.filter(is_availabe=True)
    )
   )
   
   context={
      'vendor':Vendor,
      'category':category,
   }
   return render(request,'marketplace/vendor_detail.html',context)
