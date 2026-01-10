from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404


from . import models
from . import forms


class ArchivesListView(generic.ListView):
    model = models.Archives
    template_name = "archives/archive_list.html"
    context_object_name = "archives"


class ArchiveDetailView(generic.DetailView):
    model = models.Archives
    template_name = "archives/archive_detail.html"
    context_object_name = "archive"


class ArchiveCommentCreate(generic.CreateView):
    model = models.CommentArchive
    form_class = forms.ArchiveCommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        archive_id = int(self.kwargs["archive_id"])
        archive = get_object_or_404(models.Archives, id=archive_id)

        obj.archive = archive

        return super().form_valid(form)
