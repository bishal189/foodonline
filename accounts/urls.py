
from django.urls import path,include
from . import views

urlpatterns = [

    path('registerUser/', views.registerUser,name='registerUser'),
    path('registerVendor/', views.registerVendor,name='registerVendor'),

    # for login logout and dashboard
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('myaccount/', views.myaccount,name='myaccount'),
    path('myaccount/', views.myaccount,name='myaccount'),
    path('custdashboard/', views.custdashboard,name='custdashboard'),
    path('vendordashboard/', views.vendordashboard,name='vendordashboard'),
    # path('dashboard/', views.dashboard,name='dashboard'),
   
   
]
