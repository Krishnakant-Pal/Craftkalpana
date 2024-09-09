from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,CartItem
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import Http404


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    
    return cart

def _calculate_cart_totals(request):
    total = quantity = gst = grand_total = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            print(cart,cart_items)
        
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        
        gst = (18 * total) / 100  
        grand_total = total + gst

        return total, quantity, cart_items, gst, grand_total
    except ObjectDoesNotExist:
        return total, quantity, None, gst, grand_total



def add_cart(request,product_id):
    product = Product.objects.get(pk=product_id)

    # fetching or creating a cart
    try:
        cart = Cart.objects.get(cart_id =_cart_id(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)    
        )
        cart.save()
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(product=product, user=request.user)
        
        if cart_items.exists():
            # If the product is already in the cart, update the quantity of the first item
            cart_item = cart_items.first()  # Get the first matching CartItem
            cart_item.quantity += 1
            cart_item.save()

            # Consolidate any additional CartItem objects if there are multiple
            for item in cart_items[1:]:
                cart_item.quantity += item.quantity
                item.delete()
            cart_item.save()
        
        else:
            # If not present in the cart, create a new cart item
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                user=request.user,
            )
            cart_item.save()

    else:
        # fetching or adding the items in the cart
        try:
            cart_item = CartItem.objects.get(product=product,cart=cart)
            cart_item.quantity += 1
            cart_item.save()

        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
            cart_item.save()

    return redirect('cart')

def remove_cart(request,product_id,cart_item_id):
    product = get_object_or_404(Product,id=product_id)
    try: 
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product,user=request.user,id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_item = CartItem.objects.get(product=product,cart=cart)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            
    except CartItem.DoesNotExist:
        raise Http404("Cart item not found.")
    
    except Cart.DoesNotExist:
        raise Http404("Cart not found.")
    return redirect('cart')

def remove_cart_item(request,product_id,cart_item_id):
    product = get_object_or_404(Product,id=product_id)
    # If user is logged in then fetch cart items using user
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user,id=cart_item_id)
    else:
        # If user is not logged in then fetch cart items using cart_id 
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product_id, cart=cart,id=cart_item_id)

    cart_item.delete()
    return redirect('cart')


def cart(request,total=0,quantity=0,cart_items=None):
    total, quantity, cart_items, gst, grand_total = _calculate_cart_totals(request)
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total':grand_total,
        'gst': gst,
    }
    
    return render(request,'store/cart.html',context)

@login_required(login_url = 'login')
def checkout(request,total =0,quantity =   0): 
    total, quantity, cart_items, gst, grand_total = _calculate_cart_totals(request)
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total':grand_total,
        'gst': gst,
    }
    return render(request,'store/checkout.html',context)    