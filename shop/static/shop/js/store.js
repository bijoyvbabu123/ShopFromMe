// customer = "request.user"
// link = "link to the view"


// when the document is ready, the items that are already in the cart will have the quantity control panel instead of the "add to cart" button
$(document).ready(function() {
    $.ajax({
        type: 'GET',
        timeout: 0,
        url: link,
        data: {
            'customer': customer,
            'action':'cartitems'
        },
        success: function(response) {

            $('#allproducts').children().each(function() {   // this is for looping through each child element .each()
                var id = $(this).attr('data-productid')
                if(id in response) {
                    //console.log(id, 'qty', response[id], typeof response[id]);
                    //$(this).children('.card').children('.card-body').children('.addtocart').attr("style", "display: none !important");
                    //var ele = '.addtocart'+id
                    $('.addtocart'+id).attr("style", "display: none !important");
                    //$(this).children('.card').children('.card-body').children('.numberpanel').children('.row').children('#quantity').children('.quantity').html(response[id]);
                    $('.quantity'+id).html(response[id])
                }
                else {
                    //$(this).children('.card').children('.card-body').children('.numberpanel').attr("style", "display: none !important");
                    $('.numberpanel'+id).attr("style", "display: none !important");
                }
            })
        },
        error: function(response) {
            console.log("error")
        }
    })
})