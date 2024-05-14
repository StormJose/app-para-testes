# Create your views here.
# payments/views.py

from django.shortcuts import render, redirect
from .models import Payment
from orders.models import Order
from django.contrib.auth.decorators import login_required

@login_required
def process_payment(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    payment = Payment.objects.create(
        order=order,
        user=request.user,
        amount=order.total_price,
        successful=True  # Simulating a successful payment
    )
    return render(request, 'payments/payment_success.html', {'payment': payment})

def payment_success(request):
    return render(request, 'payments/payment_success.html')
