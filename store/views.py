from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from carts.models import CartItem
from carts.views import _cart_id
from django.db.models import Q


def store(request, category_slug=None):

    categories = None
    products = None

    # === GET PRODUCTS BY CATEGORY === # 
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)

        # === CUSTOMIZE THE PAGINATOR === #
        paginator = Paginator(products, 6) # How many products we want to show for one page
        page = request.GET.get('page') # http://127.0.0.1:8000/store/?page=2
        paged_products = paginator.get_page(page)

        product_count = products.count()
    else:
        # === GET ALL PRODUCTS == #
        products = Product.objects.all().filter(is_available=True).order_by('id')
        
        # === CUSTOMIZE THE PAGINATOR === #
        paginator = Paginator(products, 6) # How many products we want to show for one page
        page = request.GET.get('page') # http://127.0.0.1:8000/store/?page=2
        paged_products = paginator.get_page(page)
        
        product_count = products.count()

    context = {'products': paged_products, 'product_count': product_count}

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):    
    
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    # === CHECK IS THE PRODUCT IN CART === #
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()

    context = {
        'product': product,
        'in_cart': in_cart
    }
    
    return render(request, 'store/product_detail.html', context)


# === SEARCH PRODUCTS === #
def search(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        # === Check that keyword is not None(blank)
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(product_name__icontains=keyword) | Q(description__icontains=keyword))

            # === CUSTOMIZE THE PAGINATOR === #
            paginator = Paginator(products, 6) # How many products we want to show for one page
            page = request.GET.get('page') # http://127.0.0.1:8000/store/?page=2
            paged_products = paginator.get_page(page)
        
            product_count = products.count()

    context = {'products': paged_products, 'product_count': product_count}

    return render(request, 'store/store.html', context)
