from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Order
from .forms import OrderForm


def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).order_by('-orderDate')
    return render(request, 'order/customer_orders.html', {
        'customer': customer,
        'orders': orders
    })


def create_order(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer
            order.save()
            return redirect('customer_orders', customer_id=customer.id)
    else:
        form = OrderForm(initial={'customer': customer})

    return render(request, 'order/create_order.html', {
        'form': form,
        'customer': customer
    })