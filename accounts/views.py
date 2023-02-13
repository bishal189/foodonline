from django.shortcuts import render,redirect
from  .form import *
from django.contrib import messages
from vendor.form import *
from .models import Userprofile
# Create your views here.

def registerUser(request): 
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)

        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.customer
            user.save()
            messages.success(request, 'Your account has been registered sucessfully!');
            return redirect('registerUser')
        else:
            print('invalid')
            print(form.errors)    
    else:
        form=UserForm()
    parms={
        'form':form,
    }
    return render(request,'accounts/register.html',parms)




def registerVendor(request):
    if request.method == 'POST':
        # a store the data and create a user
        form=UserForm(request.POST)
        v_form=VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.vendor
            user.save()
            vendor=v_form.save(commit=False)
            vendor.user=user
            user_profile=Userprofile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()
            messages.success(request, 'Your account has been registered sucessfully! please wait for approval');
            return redirect('registerUser')

        
        else:
            print('invalid')
            print(form.errors)  

    else:
        
        form=UserForm()
        v_form=VendorForm()
    
    parms={
        'form':form,
        'v_form':v_form,
    }
    print(parms)
    return render(request,'accounts/registerVendor.html',parms)















    return render(request,'accounts/registerVendor.html')