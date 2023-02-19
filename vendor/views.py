from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import  VendorForm
from accounts.forms import Userprofileform
from accounts.models import Userprofile
from .models import vendor
from django.contrib import messages
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from Menu.models import Category
from Menu.models import  Fooditem
from accounts.views import check_role_vendor,check_role_customer
from Menu.forms import Categoryform
# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_vendor)
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







@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menubuilder(request):
    Vendor=vendor.objects.get(user=request.user)
    # above code will give login vendor
    categories=Category.objects.filter(vendor=Vendor).order_by('created_at')
    context={
        'category':categories
    }

    return render(request,'vendor/menu_builder.html',context)



@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def fooditems_by_category(request,pk=None):
    Vendor=vendor.objects.get(user=request.user)
    category=get_object_or_404(Category,pk=pk)
    fooditems=Fooditem.objects.filter(vendor=Vendor, Category=category)
    context={
        'fooditems':fooditems,
        'category':category
    }


    return render(request,'vendor/fooditems_by_category.html',context)    






def add_category(request):
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            category_name=form.cleaned_data['category_name']
            category=form.save(commit=False)
            category.vendor=vendor.objects.get(user=request.user)
            category.slug=slugify(category_name)
            form.save()
            messages.success(request,'category added sucessfully!')
            return redirect('menubuilder')
        else:
            print(form.errors) 
    
    
    else:        
        form=Categoryform()
    context={
        'form':form
    }
    return render(request,'vendor/add_category.html',context)



def edit_category(request ,pk=None):
    category=get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = Categoryform(request.POST,instance=category)
        if form.is_valid():
            category_name=form.cleaned_data['category_name']
            category=form.save(commit=False)
            category.vendor=vendor.objects.get(user=request.user)
            category.slug=slugify(category_name)
            form.save()
            messages.success(request,'updated sucessfully!')
            return redirect('menubuilder')
        else:
            print(form.errors) 
    else:
         form=Categoryform(instance=category)
    context={
        'form':form,
        'category':category,
    }     

    return render(request,'vendor/edit_category.html',context)    




def delete_category(request,pk=None):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    messages.success(request,'deleted sucessfully!')
    return redirect('menubuilder')

