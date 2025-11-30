from django.shortcuts import render
from django.views import generic

from . import models

class ProductListView(generic.ListView):
    model = models.Products
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = models.Products
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    