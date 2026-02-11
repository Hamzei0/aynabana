from django.contrib import admin

from . import models


class CommentsInLine(admin.TabularInline):
    model = models.CommentArticle
    fields = ["text", "author", "stars", "active"]
    extra = 1


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "datetime_modified", "active"]
    inlines = [
        CommentsInLine,
    ]


@admin.register(models.CommentArticle)
class CommentArticleAdmin(admin.ModelAdmin):
    list_display = ["author", "article", "text", "stars", "active"]
