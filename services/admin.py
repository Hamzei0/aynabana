from django.contrib import admin

from . import models

class ServiceImagesInLine(admin.TabularInline):
    model = models.ServicesImage
    fields = ['image',]
    extra = 1

@admin.register(models.ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title',]
    
    inlines = [
        ServiceImagesInLine,
    ]

@admin.register(models.ServicesImage)
class ServicesImageAdmin(admin.ModelAdmin):
    list_display = ['service','image']
