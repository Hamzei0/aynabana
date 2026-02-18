from django.views import generic

from . import models


class Services(generic.ListView):
    model = models.Service
    template_name = "services/services.html"
    context_object_name = "services"
    ordering = ["-datetime_created"]
