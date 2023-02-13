from django.shortcuts import render,redirect
from  .form import *
from django.contrib import messages
# Create your views here.

def registerUser(request): 
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)

        if form.is_valid():
            password=form.cleaned_data['password']
            user=form.save(commit=False)
            user.set_password(password)
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