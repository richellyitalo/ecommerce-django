from django.urls import path
from .views import HomeView, ProductDetail, ProductView, checkout,\
    add_to_cart, remove_from_cart


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('checkout', checkout, name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
]
