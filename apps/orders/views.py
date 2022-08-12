import re
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from apps.cart.cart import Cart



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return render(request, 'checkout.html',
                         {'order': order})

    else:
        form = OrderCreateForm
    return render(request, 'checkout.html',
                  {'cart': cart, 'form': form})