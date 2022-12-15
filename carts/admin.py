from .models import Cart, CartItem
from django.contrib import admin

# === REGISTER MODELS === #
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'is_active']
