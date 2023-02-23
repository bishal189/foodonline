
from django.urls import path,include
from . import views
from accounts import views as accountviews

urlpatterns = [
    path('',accountviews.vendordashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),
    path('menu-builder/',views.menubuilder,name='menubuilder'),
    path('menu-builder/category/<int:pk>',views.fooditems_by_category,name='fooditems_by_category'),
    
    # for add delete and edit url
    path('menu-builder/category/add/',views.add_category,name='add_category'),
    path('menu-builder/category/edit/<int:pk>',views.edit_category,name='edit_category'),
    path('menu-builder/category/delete/<int:pk>',views.delete_category,name='delete_category'),
   
    # food items curd 

    path('menu-builder/fooditems/add/', views.add_food,name='add_food'),
    path('menu-builder/fooditems/edit/<int:pk>', views.edit_food,name='edit_food'),
    path('menu-builder/fooditems/delete/<int:pk>', views.delete_food,name='delete_food'),
   


   




]
