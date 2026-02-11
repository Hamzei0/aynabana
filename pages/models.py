from django.db import models

from django.utils.translation import gettext_lazy as _


class Consulting(models.Model):

    SERVICE_CHOICES = [
        ("cabinet", _("Cabinet")),
        ("tile", _("Tile")),
        ("decoration", _("Decoration Change")),
        ("knauf", _("Knauf")),
        ("renovation", _("Full Renovation")),
    ]

    CONTACT_TIME_CHOICES = [
        ("morning", _("Morning")),
        ("noon", _("Noon")),
        ("evening", _("Evening")),
    ]

    first_name = models.CharField(max_length=30, verbose_name=_("first name"))
    last_name = models.CharField(max_length=30, verbose_name=_("last name"))

    city = models.CharField(max_length=70, verbose_name=_("city"))

    area_size = models.PositiveIntegerField(default=0, verbose_name=_("area size"))

    service_type = models.CharField(
        max_length=20, choices=SERVICE_CHOICES, verbose_name=_("service type")
    )

    contact_time = models.CharField(
        max_length=10, choices=CONTACT_TIME_CHOICES, verbose_name=_("contacttime")
    )

    note = models.TextField(verbose_name=_("note"))

    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("datetime created"),
    )
    datetime_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("datetime modified"),
    )

    class Meta:
        verbose_name = _("Consulting")
        verbose_name_plural = _("Consultings")


class ContactUs(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_("first name"))
    last_name = models.CharField(max_length=30, verbose_name=_("last name"))

    phone_number = models.CharField(max_length=15, verbose_name=_("phone number"))

    note = models.TextField(verbose_name=_("note"))

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("ContactUss")
