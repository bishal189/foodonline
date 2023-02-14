from django.shortcuts import render,redirect,HttpResponse
from  .form import *
from django.contrib import messages,auth
from vendor.form import *
from .models import Userprofile
from .utils import detect_user
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
# Create your views here.

# restrict the vandor from accessing the customer page
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied    

# restrict the customer from accessing the vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied   







def registerUser(request): 
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in!');
        return redirect('myaccount')
    elif request.method == 'POST':
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
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in!');
        return redirect('myaccount')

    elif request.method == 'POST':
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



def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in!');
        return redirect('myaccount')
    elif request.method  == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        # build function
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in.')
            return redirect('myaccount')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')

    return render(request,'accounts/login.html')



def logout(request):
    auth.logout(request)
    messages.info(request,'You are logged out.')
    return redirect('login')


@login_required(login_url='login')
def myaccount(request):
    user=request.user
    redirecturl=detect_user(user)
    return redirect(redirecturl)


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custdashboard(request):
    return render(request,'accounts/custdashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendordashboard(request):
    return render(request,'accounts/vendordashboard.html')



