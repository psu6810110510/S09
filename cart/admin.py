from django.contrib import admin
from cart.models import CartItem
# Register your models here.
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["user","product","qty"]
    list_filter = ["user"]
    auto_complete_fields = ["product"]