from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_user_product')

        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    qty = models.PositiveIntegerField(default=1)