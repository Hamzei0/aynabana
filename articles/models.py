from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

import uuid


def Article_image_upload_to(instance, filename):
    return f"article/main_image/{uuid.uuid4()}_{filename}"


class Article(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )

    image = models.ImageField(
        upload_to=Article_image_upload_to, blank=True, verbose_name=_("image")
    )

    title = models.CharField(max_length=70, verbose_name=_("title"))
    category = models.CharField(max_length=70, verbose_name=_("category"))
    text = models.TextField(verbose_name=_("text"))

    active = models.BooleanField(
        default=False,
        verbose_name=_("active"),
    )

    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("datetime created"),
    )
    datetime_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("datetime modified"),
    )

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return f"title: {self.title}"
