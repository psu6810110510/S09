from django.http.response import JsonResponse
from accounts.models import AuthToken

def token_required(view):
    def wrapper(request, *args, **kwargs):
        key = request.headers.get("Authorization", "").removeprefix("Token ")
        token = AuthToken.objects.filter(key=key).select_related("user").first()
        if token is None:
            return JsonResponse({"error": "Invalid token"}, status=401)
        request.user = token.user
        return view(request, *args, **kwargs)
    return wrapper