from django.shortcuts import render
from django.views import generic

from . import models

class ServiceListView(generic.ListView):
    model = models.ServicesModel
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    
