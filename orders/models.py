from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.TextField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default="PENDING")
    created = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField()