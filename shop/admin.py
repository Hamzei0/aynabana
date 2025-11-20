from django.contrib import admin

from . import models

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']
