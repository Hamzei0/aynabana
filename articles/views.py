from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from . import models
from . import forms


class ArticlesListView(generic.ListView):
    model = models.Article
    template_name = "articles/articles_list.html"
    context_object_name = "articles"
    paginate_by = 6


class ArticleDetailView(generic.DetailView):
    model = models.Article
    template_name = "articles/articles_detail.html"
    context_object_name = "article"
    queryset = models.Article.article_filter.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = self.object

        related_articles = models.Article.objects.filter(
            category=article.category, active=True
        ).exclude(pk=article.pk)[:3]

        context["related_articles"] = related_articles

        latest_articles = (
            models.Article.objects.filter(active=True)
            .only("title", "pk")
            .exclude(pk=article.pk)
            .order_by("-datetime_created")[:4]
        )
        context["latest_articles"] = latest_articles

        return context


class CommentCreate(generic.CreateView):
    model = models.CommentArticle
    form_class = forms.CommentForm
    template_name = "articles/articles_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs.get("article_id")
        context["article"] = get_object_or_404(models.Article, id=article_id)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        article_id = int(self.kwargs["article_id"])

        article = get_object_or_404(models.Article, id=article_id)

        obj.article = article

        return super().form_valid(form)
