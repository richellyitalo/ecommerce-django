from django.shortcuts import render, HttpResponse
from .models import Item
from django.views.generic import ListView


class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product-page.html', context)


def checkout(request):
    return render(request, 'checkout-page.html')
