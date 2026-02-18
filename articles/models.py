from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.conf import settings

from ckeditor.fields import RichTextField

import uuid


def article_image_upload_to(instance, filename):
    return f"article/main_image/{uuid.uuid4()}_{filename}"


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)


class Article(models.Model):

    CATEGORY_CHOICES = [
        ("Renovation", _("Renovation")),
        ("Cabinet", _("Cabinet")),
        ("Knauf", _("Knauf")),
        ("InteriorDesign", _("Interior Design")),
        ("Other", _("Other")),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )

    image = models.ImageField(
        upload_to=article_image_upload_to, blank=True, verbose_name=_("image")
    )

    title = models.CharField(max_length=70, verbose_name=_("title"))
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name=_("category")
    )

    text = RichTextField(verbose_name=_("text"))
    short_text = models.CharField(max_length=50, verbose_name=_("short text"))

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

    # manager
    objects = models.Manager()
    article_filter = ActiveManager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.pk])

    def __str__(self):
        return f"title: {self.title}"


class CommentArticle(models.Model):
    PRODUCT_STARS = [
        (1, _("very bad")),
        (2, _("bad")),
        (3, _("normal")),
        (4, _("good")),
        (5, _("perfect")),
    ]

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("article"),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="article_comments",
        verbose_name=_("author"),
    )

    text = models.TextField(verbose_name=_("text"))
    active = models.BooleanField(
        default=False,
        verbose_name=_("active"),
    )
    stars = models.IntegerField(
        choices=PRODUCT_STARS,
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
        verbose_name = _("Comment Article")
        verbose_name_plural = _("Comments Article")
        ordering = ["-datetime_modified"]

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.article.id])
