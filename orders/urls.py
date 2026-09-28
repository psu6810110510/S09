from django.urls import path
from . import views

app_name = "orders"
urlpatterns =  [
    path("checkout",views.check_view,name="checkout"),
    path("orders",views.order_history,name="order-history"),
    path("orders/<int:order_id>",views.order_detail,name="order_detail")

]