
from django.urls import path,include
from . import views
from accounts import views as accountviews

urlpatterns = [
    path('',accountviews.vendordashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),
   

   
]
