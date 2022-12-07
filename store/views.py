from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def store(request, category_slug=None):

    categories = None
    products = None

    # === GET PRODUCTS BY CATEGORY === # 
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        # === GET ALL PRODUCTS == #
        products = Product.objects.filter(is_available=True)
        product_count = products.count()

    context = {'products': products, 'product_count': product_count}

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):    
    
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)