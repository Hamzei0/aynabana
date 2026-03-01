from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages

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

    def form_valid(self, form):
        messages.success(self.request, _("Your messages successfully submitted."))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Error ! Plaese try agane."))
        return super().form_invalid(form)


class Consulting(generic.CreateView):
    model = models.Consulting
    form_class = forms.ConsultingForm
    template_name = "pages/consulting.html"
    success_url = reverse_lazy("consulting")

    def form_valid(self, form):
        messages.success(
            self.request, _("Your consulting request successfully submitted.")
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Error ! Plaese try agane."))
        return super().form_invalid(form)
