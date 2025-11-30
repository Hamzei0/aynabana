from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from . import forms
from . import models

class ProductListView(generic.ListView):
    model = models.Products
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = models.Products
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = forms.CommentForm()
        return context

class CommentCreate(generic.CreateView):
    model = models.CommentProduct
    form_class = forms.CommentForm
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(models.Products, id=product_id)   
        
        obj.product = product 
        
        return super().form_valid(form)
        
    