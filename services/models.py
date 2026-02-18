from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid


def services_image_upload_to(instance, filename):
    return f"services/services_image/{uuid.uuid4()}_{filename}"


class Service(models.Model):

    SERVICE_CHOICES = [
        ("cabinet", _("Cabinet")),
        ("knauf", _("Knauf")),
        ("decoration", _("Decoration")),
    ]

    service_type = models.CharField(
        max_length=20, choices=SERVICE_CHOICES, verbose_name=_("service type")
    )

    image = models.ImageField(
        upload_to=services_image_upload_to, verbose_name=_("image")
    )

    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("datetime created"),
    )
    datetime_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("datetime modified"),
    )

    def __str__(self):
        return self.get_service_type_display()
