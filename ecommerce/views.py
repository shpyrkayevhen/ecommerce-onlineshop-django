from django.shortcuts import render
from store.models import Product

def home(request):

    # === QUERY TO THE DB === # 
    products = Product.objects.all().filter(is_available=True)
    context = {'products': products}
    
    return render(request, 'home.html', context)