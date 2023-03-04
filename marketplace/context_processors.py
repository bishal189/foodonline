from .models import Cart
from Menu.models import Fooditem

def get_cart_counter(request):
    cart_counter=0
    if request.user.is_authenticated:
        try:
            cart_items=Cart.objects.filter(user=request.user,)
            if cart_items:
                for cart_item in cart_items:
                    cart_counter+=cart_item.quantity
            


            else:
                cart_counter=0
        except:
            cart_counter=0            

    

    return dict(cart_counter=cart_counter)




def get_cart_amounts(request):
    subtotal=0
    tax=0
    grand_total=0
    if request.user.is_authenticated:
        cart_items=Cart.objects.filter(user=request.user)
        for item in cart_items:
            food_item=Fooditem.objects.get(pk=item.fooditem.id)
            subtotal+= (food_item.price *item.quantity)

        grand_total=subtotal+tax
    # print(subtotal)
    # print(grand_total)    
    return dict(subtotal=subtotal,tax=tax,grand_total=grand_total)


