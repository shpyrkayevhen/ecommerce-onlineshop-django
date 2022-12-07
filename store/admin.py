from .models import Product
from django.contrib import admin


# === REGISTER MODEL === #
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'category', 'is_available']
    prepopulated_fields = {
        'slug': ['product_name']
    }
