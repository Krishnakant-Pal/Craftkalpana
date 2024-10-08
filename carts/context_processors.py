from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # If user is logged in then filter out with user 
            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
            else:
                # If user not logged in then filter out with cart 
                cart = Cart.objects.filter(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)