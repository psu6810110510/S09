from django.contrib import admin
from shop.models import Product
from django.utils.html import format_html

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","thumb","price","is_active"]
    search_fields = ["name"]

    @admin.display(description="รูป")
    def thumb(self,obj):
        if obj.image :
            return format_html('<img src ="{}"width = "50">',obj.image.url)

        return "-"