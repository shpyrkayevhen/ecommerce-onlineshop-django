from django.core.validators import MinValueValidator
from store.models import Product
from django.db import models


class Cart(models.Model):
    cart_id = models.CharField(max_length=252, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product.product_name

    # === CALCULATE TOTAL PRICE FOR INDIVIDUAL CARTITEM === #
    def sub_total(self) -> float:
        return self.product.price * self.quantity