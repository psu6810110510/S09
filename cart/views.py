import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cart.models import CartItem
from shop.models import Product
from django.views.decorators.http import require_http_methods
from accounts.decorators import token_required

# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
@token_required
def cart_add(request):
    data = json.loads(request.body)
    product_id = data.get("product_id")
    product = get_object_or_404(Product,id=product_id,is_active=True)
    qty = data.get("qty",1)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product, defaults={"qty":qty})
    if not created:
        item.qty += qty
        item.save()
    return JsonResponse({"qty":qty})

@require_http_methods(["GET"])
@token_required
def cart_detail(request):
    items = (CartItem.objects.filter(user=request.user).select_related("product"))
    results = []
    total = 0
    for i in items:
        subtotal = i.qty * i.product.price
        cart={
            "product_id":i.product.id,
            "name":i.product.name,
            "qty":i.qty,
            "image": request.build_absolute_uri(i.product.image.url) if i.product.image else None,
            "subtotal":str(subtotal)
        }
        results.append(cart)
        total += subtotal
    return JsonResponse({"items":results,"total":str(total)})

@csrf_exempt
@require_http_methods(["POST"])
@token_required
def cart_remove(request):
    data = json.loads(request.body)
    product = get_object_or_404(Product,id=data.get("product_id"),is_active=True)
    CartItem.objects.filter(user=request.user, product=product).delete()
    return JsonResponse({"deleted":True})