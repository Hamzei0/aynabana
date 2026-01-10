from django.contrib import admin

from . import models


class CommentsInLine(admin.TabularInline):
    model = models.CommentArchive
    fields = ["text", "author", "stars", "active"]
    extra = 1


@admin.register(models.Archives)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "active"]
    inlines = [
        CommentsInLine,
    ]


@admin.register(models.CommentArchive)
class CommentArchiveAdmin(admin.ModelAdmin):
    list_display = ["author", "archive", "text", "stars", "active"]
