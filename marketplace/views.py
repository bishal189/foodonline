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
    vendors=vendor.objects.filter(is_approved=True,user__is_active=True)
    vendor_count=vendors.count()

    context={
        'vendors':vendors,
        'vendor_count':vendor_count
    }
    return render(request,'marketplace/listing.html',context)


def vendor_details(request,vendor_slug):
    Vendor=vendor.objects.get(vendor_slug=vendor_slug)
    categories=Category.objects.filter(vendor=Vendor).prefetch_related(
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
        'categories':categories,
        'cart_items':cart_items,
    }
    return render(request,'marketplace/list_details.html',context)    


def add_to_cart(request,food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            try:
                # check the food item exist 
                food_item=Fooditem.objects.get(id=food_id)
                # check the if the user already added that food to the cart
                try:
                    chk_cart=Cart.objects.get(user=request.user,fooditem=food_item)
                    # increase the cart quantity
                    chk_cart.quantity+=1
                    chk_cart.save()
                    return JsonResponse({'status':'Success','message':'Increased the cart item successfuly','cart_counter':get_cart_counter(request),'qty':chk_cart.quantity})


                except:
                    chk_cart=Cart.objects.create(
                        user=request.user,
                        fooditem=food_item,
                        quantity=1,
                    )
                    return JsonResponse({'status':'Success','message':'created new cart and added sucessfully','cart_counter':get_cart_counter(request),'qty':chk_cart.quantity})

            except:

               return JsonResponse({'status':'Failed','message':'This food items does not exist!'})
            
        else:

            return JsonResponse({'status':'Failed','message':'Invalid request!'})

    
    else:

       return JsonResponse({'status':'login_required','message':'please login to continue'})







def decrease_cart(request,food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            try:
                # check the food item exist 
                food_item=Fooditem.objects.get(id=food_id)
                # check the if the user already added that food to the cart
                try:
                    chk_cart=Cart.objects.get(user=request.user,fooditem=food_item)
                    # decrease the cart quantity
                    if chk_cart.quantity >1:
                      chk_cart.quantity-=1
                      chk_cart.save()
                      
                    else:
                        chk_cart.delete()
                        chk_cart.quantity=0
                    return JsonResponse({'status':'Success','cart_counter':get_cart_counter(request),'qty':chk_cart.quantity})    

                except:
                    return JsonResponse({'status':'Failed','message':'You do not have food item in your cart!'})

            except:

               return JsonResponse({'status':'Failed','message':'This food items does not exist!'})
            
        else:

            return JsonResponse({'status':'Failed','message':'Invalid request!'})

    
    else:

       return JsonResponse({'status':'login_required','message':'please login to continue'})




  
