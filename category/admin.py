from django.contrib import admin
from .models import Category

# === REGISTER MODELS === #

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {
        'slug': ['category_name']
    }


