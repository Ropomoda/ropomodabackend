from rest_framework.exceptions import  NotAcceptable

def get_quantity_from_request(request , product):
    try:
        quantity = int(request.data["quantity"])
    except Exception as e:
        raise NotAcceptable("Please Enter your quantity")

    if quantity > product.inventory:
        raise NotAcceptable("Your Entered quantity is more then inventory")
    if quantity > product.max_quantity:
        raise NotAcceptable("Your Entered quantity is more then max allowed quantity")
    return quantity