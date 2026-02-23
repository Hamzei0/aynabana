from django import forms

from . import models


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = ["first_name", "last_name", "phone_number", "note"]


class ConsultingForm(forms.ModelForm):
    class Meta:
        model = models.Consulting
        fields = [
            "first_name",
            "last_name",
            "city",
            "area_size",
            "service_type",
            "contact_time",
            "note",
        ]
