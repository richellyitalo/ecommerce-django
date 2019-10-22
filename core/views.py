from django.shortcuts import render, HttpResponse
from .models import Item
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ProductView(ListView):
    model = Item
    template_name = 'products.html'


class ProductDetail(DetailView):
    model = Item
    template_name = 'product.html'


def checkout(request):
    return render(request, 'checkout-page.html')
