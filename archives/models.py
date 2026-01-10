from django.db import models
from django.shortcuts import reverse

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)


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


class CommentArchive(models.Model):
    Archive_STARS = [
        ("1", _("very bad")),
        ("2", _("bad")),
        ("3", _("normal")),
        ("4", _("good")),
        ("5", _("perfect")),
    ]

    archive = models.ForeignKey(
        Archives,
        on_delete=models.CASCADE,
        related_name="archive_comments",
        verbose_name="archive",
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="archive_author",
        verbose_name=_("author"),
    )

    text = models.TextField(verbose_name=_("text"))
    active = models.BooleanField(
        default=False,
        verbose_name=_("active"),
    )
    stars = models.CharField(
        max_length=1,
        choices=Archive_STARS,
        verbose_name=_("stars"),
    )

    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("datetime created"),
    )
    datetime_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("datetime modified"),
    )

    # manager
    objects = models.Manager()
    comment_filter = ActiveManager()

    class Meta:
        verbose_name = _("CommentArchive")
        verbose_name_plural = _("CommentArchives")

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
