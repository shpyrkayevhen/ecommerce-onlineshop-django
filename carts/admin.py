from .models import Cart, CartItem
from django.contrib import admin

# === REGISTER MODELS === #
@admin.register(Cart)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CategoryAdmin(admin.ModelAdmin):
    pass
