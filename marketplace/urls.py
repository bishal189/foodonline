
from django.urls import path
from . import views
urlpatterns = [
    path('',views.marketplace,name='Marketplace'),
    path('<slug:vendor_slug>',views.vendor_details,name='vendor_details'),
    # increase cart using ajax request
    path('add_to_cart/<int:food_id>',views.add_cart,name='add_cart'),
    # decrease cart using ajax request
    path('decrease_to_cart/<int:food_id>',views.decrease_to_cart,name='decrease_to_cart'),
   
]
