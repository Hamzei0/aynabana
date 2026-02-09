from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/dashboard.html"
