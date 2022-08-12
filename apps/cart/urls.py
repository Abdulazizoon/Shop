from django.urls import include, path
from . import views
from .views import cart_add, cart_detail, item_clear, cart_clear
from apps.orders.views import order_create

urlpatterns = [
    path('cart-detail/', cart_detail, name='cart_detail'),
    path('add/<int:pk>/', cart_add, name='cart_add'),
    path('item_clear/<slug:slug>/', item_clear, name='item_clear'),
    path('cart_clear/', cart_clear, name='cart_clear'),
    path(r'^create/$', order_create, name='order_create')
]
