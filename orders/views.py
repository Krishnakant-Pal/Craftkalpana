from django.shortcuts import render,redirect
from carts.models import CartItem
from .forms import OrderForm
from .models import Order
from carts.views import _calculate_cart_totals
import datetime

def payments(request):
    total, quantity, cart_items, gst, grand_total = _calculate_cart_totals(request)
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total':grand_total,
        'gst': gst,
    }
    return render(request,'orders/payments.html',context)

def order_place(request):
    current_user = request.user
    
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    print(cart_count)

    # if cart is empty return to store
    if cart_count <= 0:
        return redirect('store')
    
    total, quantity, cart_items, gst, grand_total = _calculate_cart_totals(request)


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.pincode = form.cleaned_data['pincode']
            data.email = current_user.email
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.order_total = grand_total
            data.gst = gst
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            print("generating order number...")
            # Generate order number using date and id
            year = int(datetime.date.today().strftime('%Y'))
            month = int(datetime.date.today().strftime('%m'))
            day = int(datetime.date.today().strftime('%d'))
            d = datetime.date(year,month,day)
            current_date = d.strftime("%Y%m%d") 
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'gst': gst,
                'grand_total': grand_total,
            }
            return render(request, 'orders/payments.html', context)
        else:
            context = [
                "form"
            ]
            print(form.errors.as_text)
    return redirect('checkout')
    


    