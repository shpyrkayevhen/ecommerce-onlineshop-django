from django.core.validators import MinValueValidator
from category.models import Category
from django.db import models

# === CREATE MODELS === # 
class Product(models.Model):
    # === CREATE RELATION SHIP MANY-TO-ONE === # 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=252, unique=True)
    slug = models.SlugField(max_length=252, unique=True)
    description = models.TextField(max_length=505, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    images = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    # === NAME REPRESENTATION INSIDE ADMIN === # 
    def __str__(self) -> str:
        return str(self.product_name)
    

    
    # === URL FOR GETTING SINGLE PRODUCT === #
    # from django.urls import reverse
    # def get_url(self):
    #     return reverse('product-detail/', args=[self.category.slug, self.slug])

    # But I always use: "{% url 'product_detail' product.category.slug product.slug %}"