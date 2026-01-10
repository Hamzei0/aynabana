from django.shortcuts import render
from django.views import generic

from . import models


class ArchivesListView(generic.ListView):
    model = models.Archives
    template_name = "archives/archive_list.html"
    context_object_name = "archives"
