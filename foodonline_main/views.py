
from vendor.models import vendor
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    Vendor=vendor.objects.filter(is_approved=True,user__is_active=True)[:8]
    context={
        'vendor':Vendor,
    }
    # print(Vendor,'*********')
    return render(request,'home.html',context)