from django.contrib import admin
from accounts.models import AuthToken, Profile

# Register your models here.
@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ["user", "key", "created"]
    readonly_fields = ["key", "created"]
    search_fields = ["user__username"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "address"]
    search_fields = ["user__username", "phone"]

