from django.shortcuts import render

# Create your views here.

from .models import Order, OrderItem, Customer

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'sop/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    items = OrderItem.objects.filter(order=order)
    customer = Customer.objects.get(id=order.customer_id)
    return render(request, 'sop/order_detail.html', {'order': order, 'items': items, 'customer': customer})
