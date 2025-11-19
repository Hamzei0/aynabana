from django.contrib import admin

from . import models

@admin.register(models.ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    model = models.ServicesModel
    
