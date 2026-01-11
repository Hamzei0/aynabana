from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class AboutUsView(generic.TemplateView):
    template_name = "about_us.html"


class PrivacyPolicy(generic.TemplateView):
    template_name = "privacy_policy.html"


class ContactUs(generic.CreateView):
    model = models.ContactUs
    form_class = forms.ContactUsForm
    template_name = "pages/contact_us.html"
    success_url = reverse_lazy("contact_us")


class Consulting(generic.CreateView):
    model = models.Consulting
    form_class = forms.ConsultingForm
    template_name = "pages/consulting.html"
    success_url = reverse_lazy("consulting")
