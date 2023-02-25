from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from vendor.models import vendor
from Menu.models import Category,Fooditem
from django.db.models import Prefetch
from marketplace.models import Cart
from .context_processors import get_cart_counter

# Create your views here.

def marketplace(request):
   Vendor=vendor.objects.filter(is_approved=True,user__is_active=True)
   Vendor_count=Vendor.count()
   context={
      'vendor':Vendor,
      'vendor_count':Vendor_count
   }
   return render(request,'marketplace/listing.html',context)



def vendor_details(request,vendor_slug):
   Vendor=get_object_or_404(vendor,vendor_slug=vendor_slug)
  
   category=Category.objects.filter(vendor=Vendor).prefetch_related(
    Prefetch(
      'fooditems',
      queryset=Fooditem.objects.filter(is_availabe=True)
    )
   )
   if request.user.is_authenticated:
      cart_items=Cart.objects.filter(user=request.user)
   else:
      cart_items=None   
   
   context={
      'vendor':Vendor,
      'category':category,
      'cart_items':cart_items
   }
   return render(request,'marketplace/vendor_detail.html',context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def add_cart(request,food_id):
   if request.user.is_authenticated:
      if is_ajax(request):
         #check if the food item exist
         try:
            food_item=Fooditem.objects.get(id=food_id)
            #check if the user has already added this food to the cart
            try:
               chk_cart=Cart.objects.get(user=request.user,fooditem=food_item)
               chk_cart.quantity+=1;
               chk_cart.save()
               return JsonResponse({'status':'success','message':'increased the cart quantity','cart_count':get_cart_counter(request),'qty':chk_cart.quantity})
            except:
               chk_cart=Cart.objects.create(user=request.user,fooditem=food_item,quantity=1)  
               return JsonResponse({'status':'success','message':'Added the food to the cart!','cart_count':get_cart_counter(request),'qty':chk_cart.quantity})

         except:
            return JsonResponse({'status':'failed','message':'food doesnot exist'})

         
      else:
        return JsonResponse({'status':'failed','message':'invalid request'})
   else:   
      return JsonResponse({'status':'login_required','message':'please login to continue'})







def decrease_to_cart(request,food_id):
   if request.user.is_authenticated:
      if is_ajax(request):
         #check if the food item exist
         try:
            food_item=Fooditem.objects.get(id=food_id)
            #check if the user has already added this food to the cart
            try:
               # decrease the quantity
               
               chk_cart=Cart.objects.get(user=request.user,fooditem=food_item)
               if chk_cart.quantity>1:
                  chk_cart.quantity-=1;
                  chk_cart.save()
               else:
                  chk_cart.delete()
                  chk_cart.quantity=0;

               return JsonResponse({'status':'success','cart_count':get_cart_counter(request),'qty':chk_cart.quantity})
            except:
               
               return JsonResponse({'status':'failed','message':'you dont have that item in your cart','cart_count':get_cart_counter(request)})

         except:
            return JsonResponse({'status':'failed','message':'food doesnot exist'})

         
      else:
        return JsonResponse({'status':'failed','message':'invalid request'})
   else:   
      return JsonResponse({'status':'login_required','message':'please login to continue'})

