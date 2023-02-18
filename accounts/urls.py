
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.myaccount,name='myaccount'),
    path('registerUser/', views.registerUser,name='registerUser'),
    path('registerVendor/', views.registerVendor,name='registerVendor'),

    # for login logout and dashboard
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('myaccount/', views.myaccount,name='myaccount'),
    path('myaccount/', views.myaccount,name='myaccount'),
    path('custdashboard/', views.custdashboard,name='custdashboard'),
    path('vendordashboard/', views.vendordashboard,name='vendordashboard'),
    
    path('activate/<uidb64>/<token>/', views.activate,name='activate'),
    path('forget_password/', views.forget_password,name='forget_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate,name='reset_password_validate'),
    path('reset_password/', views.reset_password,name='reset_password'),
    path('vendor/',include('vendor.urls'))

    # path('dashboard/', views.dashboard,name='dashboard'),
   
   
]
