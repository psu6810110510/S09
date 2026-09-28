from django.urls import path
from cart import views
app_name = "cart"
urlpatterns =  [
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add', views.cart_add, name='add_cart'),
    path('cart/remove', views.cart_remove, name='remove_cart')

]