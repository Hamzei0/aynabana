from django.contrib import admin

from . import models


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "note"]


@admin.register(models.Consulting)
class ConsultingAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "city", "note"]
