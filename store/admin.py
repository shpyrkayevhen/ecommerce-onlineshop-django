from .models import Product, Variation
from django.contrib import admin


# === REGISTER MODEL === #
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'category', 'is_available']
    prepopulated_fields = {
        'slug': ['product_name']
    }


@admin.register(Variation)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    list_editable = ['is_active']
    list_filter = ['product', 'variation_category', 'variation_value']
