from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.shortcuts import get_object_or_404

from cart.forms import AddToCartProductForm

from . import forms
from . import models


class ProductListView(generic.ListView):
    model = models.Products
    template_name = "shop/product_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.copy()
        query.pop("page", None)  # حذف page قبلی
        context["querystring"] = query.urlencode()
        return context

    def get_queryset(self):
        queryset = models.Products.objects.filter(active=True)

        # -------------------
        # فیلتر بر اساس نوع (مدل آینه)
        # -------------------
        product_type = self.request.GET.get("model")
        if product_type:
            queryset = queryset.filter(type=product_type)

        # -------------------
        # جستجو
        # -------------------
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(short_description__icontains=search)
            )

        # -------------------
        # مرتب سازی
        # -------------------
        ORDERING_OPTIONS = {
            "cheap": "price",
            "expensive": "-price",
            "newest": "-datetime_created",
        }

        ordering = self.request.GET.get("ordering")
        if ordering in ORDERING_OPTIONS:
            queryset = queryset.order_by(ORDERING_OPTIONS[ordering])

        return queryset


class ProductDetailView(generic.DetailView):
    model = models.Products
    template_name = "shop/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = forms.CommentForm()
        context["add_to_cart"] = AddToCartProductForm()
        return context


class CommentCreate(generic.CreateView):
    model = models.CommentProduct
    form_class = forms.CommentForm
    template_name = "shop/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get("product_id")
        context["product"] = get_object_or_404(models.Products, id=product_id)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs["product_id"])
        product = get_object_or_404(models.Products, id=product_id)

        obj.product = product

        return super().form_valid(form)
