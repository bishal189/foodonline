$(document).ready(function(){
    $('.add_to_cart').on('click',function(e){

        //add to cart

        e.preventDefault();
        food_id=$(this).attr('data-id');
        url=$(this).attr('data-url');
        data={
            food_id:food_id,
        }
        $.ajax({
            type:'GET',
            url:url,
            // data:data,
            success:function(response){
                console.log(response)
                if (response.status =='login_required'){
                    swal(response.message,'','info').then(function(){
                        window.location='/login/'
                    })  
                   }
                else if(response.status == 'Failed'){
                    swal(response.messages,'','error')

                }
                else{
                    $('#cart_counter').html(response.cart_counter['cart_counter'])
                    $('#qty-'+food_id).html(response.qty)
                         //subtotal ,tax and grandtotal

                    applycartamounts(response.cart_amount['subtotal'],
                    response.cart_amount['tax'],
                    response.cart_amount['grand_total'])

                
                }



              

                  

            }
        })
    })

    //place the cart item qutantity on load
    $('.item-qty').each(function(){
        var the_id=$(this).attr('id')
        var qty=$(this).attr('data-qty')
        console.log(qty)
        $('#'+the_id).html(qty)
      
    })

//decrease cart item
    $('.decrease_cart').on('click',function(e){
        e.preventDefault();
        food_id=$(this).attr('data-id');
        cart_id=$(this).attr('id');
        url=$(this).attr('data-url');
        data={
            food_id:food_id,
        }
        $.ajax({
            type:'GET',
            url:url,
            data:data,
            
            success:function(response){
               console.log(response)
               if (response.status == 'login_required'){
                swal(response.message,'','info').then(function(){
                    window.location='/login/'
                })  

               }
               else if (response.status =='Failed'){
                swal(response.message,'','error')
               }
               else{
                $('#cart_counter').html(response.cart_counter['cart_counter'])
                $('#qty-'+food_id).html(response.qty)

                applycartamounts(response.cart_amount['subtotal'],
                response.cart_amount['tax'],
                response.cart_amount['grand_total'])


                if(window.location.pathname == '/cart/'){
                    removecartitem(response.qty,cart_id)
                    checkEmptycart()

                }

               
               }
              

            }
        })
    })


    //delete cart item
    $('.delete_cart').on('click',function(e){
        e.preventDefault();
        cart_id=$(this).attr('data-id');
        url=$(this).attr('data-url');
        data={
            cart_id:cart_id,
        }
        $.ajax({
            type:'GET',
            url:url,
            data:data,
            success:function(response){
 
               if (response.status == 'Failed'){
                swal(response.message,'','error')
               }
               else{
                $('#cart_counter').html(response.cart_counter['cart_counter'])
                swal(response.status,response.message,'success')
                removecartitem(0,cart_id)

                checkEmptycart()

                applycartamounts(response.cart_amount['subtotal'],
                response.cart_amount['tax'],
                response.cart_amount['grand_total'])


               }
              

            }
        })
    })




    //delete cart element if the quantity is 0
    function removecartitem(cartitemqty,cart_id){

            if (cartitemqty<=0){
                //remove the cart item element
                document.getElementById("cart-item-"+cart_id).remove()   
            }

        
       
    }


    // check if the cart is empty

    function checkEmptycart(){
        var cart_counter=document.getElementById('cart_counter').innerHTML
        if(cart_counter==0){
            document.getElementById('empty-cart').style.display='block'
        }
    }




    //apply cart amounts


    function applycartamounts(subtotal,tax,grandtotal){
      if (window.location.pathname =='/cart/'){
        $('#subtotal').html(subtotal)
        $('#tax').html(tax)
        $('#total').html(grandtotal)

      }  
     
    }


});