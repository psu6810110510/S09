from django.contrib import admin
from orders.models import Order, OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ["product","price","qty"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","user","total","status","created"]
    list_filter = ["status","created"]
    readonly_fields = ["user","address","total","status","created"]
    inlines = [OrderItemInline]