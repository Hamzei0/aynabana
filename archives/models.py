from django.db import models
from django.shortcuts import reverse

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Archives(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="author",
        verbose_name=_("author"),
    )

    title = models.CharField(max_length=100, verbose_name=_("title"))
    short_description = models.CharField(
        max_length=300, verbose_name=_("short description")
    )
    full_description = models.TextField(verbose_name=_("full description"))

    active = models.BooleanField(default=True, verbose_name=_("active"))

    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("datetime created")
    )
    datetime_modified = models.DateTimeField(
        auto_now=True, verbose_name=_("datetime modified")
    )

    class Meta:
        verbose_name = _("Archive")
        verbose_name_plural = _("Archives")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("archive_detail", args=[self.pk])
