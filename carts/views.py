from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import CartItem, Cart
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist


# === BRING SESSION ID AND SPECIFY THEM OUR CART ID=== #
def _cart_id(request): # Create privete function
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()

    # === CART ID === #
    return cart_id

def add_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    
    
    try:
        # === CREATE OR CHECK EXISTING CART | CART ID IS THE SESSION ID === #
        cart = Cart.objects.get(cart_id=_cart_id(request))
    
    except Cart.DoesNotExist:
        # === CREATE NEW CART === #
        cart = Cart.objects.create(
            cart_id = _cart_id(request),         
        )
        cart.save()
    
    
    try:
        # === CREATE/ADD OR CHECK EXISNING(+1) ITEM IN CART === #
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    
    except CartItem.DoesNotExist:
        # === CREATE CART ITEM. FIRST CLICK ON PRODUCT FOR ADDING NEW ITEM IN CART === #  
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )

    # === AFTER CLICK(ADDING ITEM) REDIRECT USER FOR CART PAGE === #
    return redirect('cart') 


def cart(request, total=0, quantity=0, cart_items=None):
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += cart_item.product.price*cart_item.quantity
            quantity += cart_item.quantity

        tax = 2 * total / 100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)