let autocomplete;

function initAutoComplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('id_address'),
        {
            types: ['geocode', 'establishment'],
            //default in this app is "IN" - add your country code
            componentRestrictions: { 'country': ['in'] },
        })
    // function to specify what should happen when the prediction is clicked
    autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry) {
        document.getElementById('id_address').placeholder = "Start typing...";
    }
    else {
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields
}


$(document).ready(function () {
    // add to cart
    $('.add_to_cart').on('click', function (e) {
        e.preventDefault();
        food_id = $(this).attr('data-id');
        data_url = $(this).attr('data-url');
        data = {
            food_id: food_id,
        }
        $.ajax({
            type:'GET',
            url: data_url, 
            success: function (response) {
                 if (response.status=='login_required'){
                   swal(response.message,'','info').then(function(){
                    window.location='/login'
                   })
                 }else if(response.status=='failed'){
                    swal(response.message,'','error')
                 }
                 else
                 {

                    $('#cart_counter').html(response.cart_count['cart_count'])
                    $('#qty-'+food_id).html(response.qty)
                 }
                
            }
        });
    })
    // decrease the cart
    $('.decrease_cart').on('click', function (e) {
        e.preventDefault();
        food_id = $(this).attr('data-id');
        data_url = $(this).attr('data-url');
        data = {
            food_id: food_id,
        }
        $.ajax({
            type:'GET',
            url: data_url, 
            success: function (response) {
                if (response.status=='login_required'){
                    swal(response.message,'','info').then(function(){
                     window.location='/login'
                    })
             

                }
                else if (response.status=='failed'){
                    swal(response.message,'','error')
                }
                else{
                    $('#cart_counter').html(response.cart_count['cart_count'])
                    $('#qty-'+food_id).html(response.qty)
                }
               
                
            }
        });
    })

    //place the cart item quantity on load
    $('.item_qty').each(function () {
       
       var  data_qty= $(this).attr('data-qty');
       var id=$(this).attr('id');
       $('#'+id).html(data_qty)
       
      
    })
     
    
});