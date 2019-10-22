from django.urls import path
from .views import HomeView, ProductDetail, ProductView, checkout


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('product/<slug>', ProductDetail.as_view(), name='product'),
    path('checkout', checkout, name='checkout')
]
