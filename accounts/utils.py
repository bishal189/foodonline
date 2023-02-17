
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings 

def detect_user(user):
    if user.role == 1:
        redirecturl= 'vendordashboard'
        return redirecturl


    elif user.role == 2:
        redirecturl='custdashboard'   
        return redirecturl 

    elif user.role == None and user.is_superadmin:
        redirecturl='/admin'
        return redirecturl    




def send_verification_email(request,user,mail_subject,email_template):
    from_email=settings.DEFAULT_FROM_EMIAL
    current_site=get_current_site(request)
    message=render_to_string(email_template,{
        'user':user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':default_token_generator.make_token(user),
    })

    to_email=user.email
    email=EmailMessage(mail_subject,message,from_email,to=[to_email])
    email.send() 


# def send_password_reset_email(request,user):
#     from_email=settings.DEFAULT_FROM_EMIAL
#     current_site=get_current_site(request)
#     mail_subject='reset your password'
#     message=render_to_string('accounts/emails/reset_password_email.html',{
#         'user':user,
#         'domain':current_site,
#         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#         'token':default_token_generator.make_token(user),
#     })

#     to_email=user.email
#     email=EmailMessage(mail_subject,message,from_email,to=[to_email])
#     email.send() 


