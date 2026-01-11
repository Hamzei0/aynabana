from django import forms

from . import models


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = ["first_name", "last_name", "phone_number", "note"]
