from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )
    is_paid = models.BooleanField(default=False, verbose_name=_("is paid"))

    first_name = models.CharField(max_length=70, verbose_name=_("first name"))
    last_name = models.CharField(max_length=70, verbose_name=_("last name"))

    phone_number = models.CharField(max_length=15, verbose_name=_("phone number"))
    address = models.CharField(max_length=300, verbose_name=_("address"))
    order_notes = models.TextField(blank=True, verbose_name=_("order notes"))

    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("datetime created"),
    )
    datetime_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("datetime modified"),
    )

    def __str__(self):
        return f"Order: {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="item", verbose_name=_("item")
    )
    product = models.ForeignKey(
        "shop.Products",
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("order items"),
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("quantity"))
    price = models.PositiveIntegerField(verbose_name=_("price"))
