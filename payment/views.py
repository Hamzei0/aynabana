import requests
import json

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from orders.models import Order


def payment_process(request):
    # get order id from session
    order_id = request.session["order_id"]
    # get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = Order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = "https://payment.zarinpal.com/pg/v4/payment/request.json"

    request_header = {"accept": "application/json", "content-type": "application/json"}

    request_data = {
        "merchant_id": settings.ZARINPAL_MERCHANT_ID,
        "amount": rial_total_price,
        "description": f"#{order.id}: {order.first_name} {order.last_name}",
        "callback_url": "127.0.0.1:8000",
    }

    response = requests.post(
        url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header
    )
