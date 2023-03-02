
from vendor.models import vendor
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    items=vendor.objects.filter(is_approved=True,user__is_active=True)[:8]
    context={
        'items':items
    }
    return render(request,'home.html',context)