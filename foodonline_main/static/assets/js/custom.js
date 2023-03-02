$(document).ready(function(){
    $('.add_to_cart').on('click',function(e){
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


    $('.decrease_cart').on('click',function(e){
        e.preventDefault();
        food_id=$(this).attr('data-id');
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
               if (response.status =='Failed'){
                swal(response.message,'','error')
               }
               else{
                $('#cart_counter').html(response.cart_counter['cart_counter'])
                $('#qty-'+food_id).html(response.qty)
               }
              

            }
        })
    })


});