from django.shortcuts import render, get_object_or_404

from orders.models import Order


def payment_process(request):
    # get order id from session
    order_id = request.session["order_id"]
    # get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = Order.get_total_price()
    rial_total_price = toman_total_price * 10
