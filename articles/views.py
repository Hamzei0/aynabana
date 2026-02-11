from django.shortcuts import render
from django.views import generic

from . import models


class ArticlesListView(generic.ListView):
    model = models.Article
    template_name = "articles/articles_list.html"
    context_object_name = "articles"
    paginate_by = 6


class ArticleDetailView(generic.DetailView):
    model = models.Article
    template_name = "articles/articles_detail.html"
    context_object_name = "article"
