
from django.urls import path
from . import views
urlpatterns = [
    path('',views.marketplace,name='Marketplace'),
    path('<slug:vendor_slug>',views.vendor_details,name='vendor_details'),
   
]
