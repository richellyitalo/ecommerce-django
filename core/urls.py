from django.urls import path
from .views import HomeView, products, checkout


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products', products, name='products'),
    path('checkout', checkout, name='checkout')
]
