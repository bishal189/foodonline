from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import  VendorForm
from accounts.forms import Userprofileform
from accounts.models import Userprofile
from .models import vendor
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
@login_required(login_url='login')
def vprofile (request):
    profile=get_object_or_404(Userprofile,user=request.user)
    vendor1=get_object_or_404(vendor,user=request.user)
    if request.method == 'POST':
        profile_form=Userprofileform(request.POST,request.FILES,instance=profile)
        vendor_form=VendorForm(request.POST,request.FILES,instance=vendor1)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request,'settings updated.')
            return redirect('vprofile')
    
        else:
           print(profile_form.errors)
           print(vendor_form.errors)
    else:

        profile_form=Userprofileform(instance=profile)
        vendor_form=VendorForm(instance=vendor1)
    context={
        'profile_form':profile_form,
        'vendor_form':vendor_form,
        'profile':profile,
        'vendor1':vendor1,
    }

    return render(request,'vendor/profile.html',context)