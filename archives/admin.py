from django.contrib import admin

from . import models


@admin.register(models.Archives)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "active"]
