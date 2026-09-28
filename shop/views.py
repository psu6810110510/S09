from itertools import count

from django.shortcuts import render
from django.http import JsonResponse
from shop.models import Product
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
def product_list(request):
    q = request.GET.get("q","")
    products = Product.objects.filter(Q(name__icontains=q),is_active=True)
    results = []
    for p in products:
        product = {
            "id":p.id,
            "name":p.name,
            "description":p.description,
            "price":str(p.price),
            "image": request.build_absolute_uri(p.image.url) if p.image else None,
        }
        results.append(product)
    return JsonResponse({"count":len(results),"results":results})
def product_detail(request,product_id):
    p = get_object_or_404(Product,id=product_id,is_active=True)
    return JsonResponse({
        "id":p.id,
        "name":p.name,
        "description":p.description,
        "price":str(p.price),
        "image": request.build_absolute_uri(p.image.url) if p.image else None,
    })