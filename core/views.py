from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages


class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'home.html'


class ProductView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'products.html'


class ProductDetail(DetailView):
    model = Item
    template_name = 'product.html'


def checkout(request):
    return render(request, 'checkout-page.html')


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Produto atualizado.')
        else:
            messages.info(request, 'Produto adicionado.')
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'Produto adicionado.')
    return redirect('core:product', slug=item.slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                user=request.user,
                item=item,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, 'Produto removido dos pedidos.')
        else:
            messages.info(request, 'O produto não está adicionado ao pedido.')
            return redirect('core:product', slug=item.slug)
    else:
        messages.info(request, 'Não é um pedido associado a você.')
        return redirect('core:product', slug=item.slug)
    return redirect('core:product', slug=item.slug)
