from django.urls import path
from .views import (
    HomeView,
    ProductDetail,
    ProductView,
    checkout,
    remove_a_quantity_from_cart,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView
)


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('checkout', checkout, name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-quantity-from-cart/<slug>/',
         remove_a_quantity_from_cart, name='remove-quantity-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
]
