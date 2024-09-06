from django.shortcuts import render,get_object_or_404
from .models import Product
from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


def store(request,category_slug=None):
    categories = None
    products = None
    # Get product by their category 
    if category_slug!= None :
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories,is_available=True).order_by('id')
        #Paginage the products
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        #Paginage the products
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context  = {
        "products": paged_products,
        "category_name": categories,
        "product_count": product_count
    }
    return render(request, 'store/store.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'product_name'  : single_product.product_name.title(),
        'in_cart'       : in_cart,
       
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'search_query' in request.GET:
        keyword = request.GET['search_query']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)