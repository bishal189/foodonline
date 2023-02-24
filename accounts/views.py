from django.shortcuts import render,redirect,HttpResponse
from  .forms import *
from django.contrib import messages,auth
from  vendor.forms import *
from .models import Userprofile
from .utils import detect_user
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from .utils import send_verification_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from vendor.models import vendor
from django.template.defaultfilters import slugify
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

            # # send verification to the user through email

            mail_subject='please activate your account'
            email_template='accounts/emails/reset_password_email.html'
            send_verification_email(request,user,mail_subject,email_template)


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
            vendor_name=v_form.cleaned_data['vendor_name']
            vendor.vendor_slug=slugify(vendor_name)+'-'+str(user.id)

            user_profile=Userprofile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()

            # # send verification to the user through email
            mail_subject='please activate your account'
            email_template='accounts/emails/account_verification_email.html'
            send_verification_email(request,user,mail_subject,email_template)

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



def activate(request,uidb64,token):
    # activate the user by setting the is_activate status to true
    
    try:
        uid=urlsafe_base64_decode(uidb64).decode() 
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,user.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Congrulations your account is activated.')
        return redirect ('myaccount')
    else: 
        messages.error(request,'invalid activation link')
        return redirect('myaccount')

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
    User=request.user
    redirecturl=detect_user(User)
    return redirect(redirecturl)


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custdashboard(request):
    return render(request,'accounts/custdashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendordashboard(request):
    # fetching profile and cover photos including stuff form userprofile

    return render(request,'accounts/vendordashboard.html')





def forget_password(request):
    if request.method == 'POST':
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email__exact= email)

            # send reset password email link
            mail_subject='Reset your password'
            email_template='accounts/emails/reset_password_email.html'
            send_verification_email(request,user,mail_subject,email_template)
            messages.success(request,'password reset link has been sent to your email address')
            return redirect ('login')
        else: 
            messages.error(request,'Account does not exist')
            return redirect('forget_password')
    return render(request,'accounts/forget_password.html')






def reset_password_validate(request,uidb64,token):
    # validate the user by decoding the token and user primary key
    try:
        uid=urlsafe_base64_decode(uidb64).decode() 
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,user.DoesNotExist):
        user=None
     
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        messages.info(request,'please reset your password')
        return redirect ('reset_password')
    else:
        messages.error(request,'this link has been expired.')
        return redirect('myaccount')





def reset_password(request):
    if request.method == 'POST':
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']
        if  password == confirm_password:
            pk=request.session.get('uid')
            user=User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active=True
            user.save()
            messages.success(request,'password reset sucessful')
            return redirect('login')
        else:
            messages.error(request,'password does not match')
            return redirect('reset_password')
  
    return render(request,'accounts/reset_password.html')
