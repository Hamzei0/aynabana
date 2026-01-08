from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class AboutUsView(generic.TemplateView):
    template_name = "about_us.html"


class PrivacyPolicy(generic.TemplateView):
    template_name = "privacy_policy.html"
