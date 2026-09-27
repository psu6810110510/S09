import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from accounts.models import AuthToken
from django.contrib.auth import authenticate, login
from accounts.decorators import token_required
from accounts.models import AuthToken,Profile
# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def register_view(request):
    data = json.loads(request.body)
    form = UserCreationForm(data)

    if form.is_valid():
        user = form.save()
        token = AuthToken.for_user(user)
        return JsonResponse({
            "username": user.username,
            "token": token.key
        }, status=201)
    return JsonResponse({"errors": form.errors}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    data = json.loads(request.body)
    user = authenticate(
        request, username=data.get("username"),
        password=data.get("password"))
    if user is None:
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    token = AuthToken.for_user(user)
    return JsonResponse({"username": user.username, "token": token.key}) 

@csrf_exempt
@require_http_methods(["POST"])
@token_required
def logout_view(request):
    AuthToken.objects.filter(user=request.user).delete()
    return JsonResponse({"ok": True})

@token_required
def me_view(request):
    return JsonResponse({
        "id": request.user.id,
        "username": request.user.username})

@csrf_exempt
@require_http_methods(["GET","PUT"])
@token_required
def profile_view(request):
    prof,_ = Profile.objects.get_or_create(user=request.user)
    if request.method == "PUT":
        data = json.loads(request.body)
        prof.phone = data.get("phone", prof.phone)
        prof.address = data.get("address", prof.address)
        prof.save()
    return JsonResponse({
        "username": request.user.username,
        "phone": prof.phone,
        "address": prof.address
    })