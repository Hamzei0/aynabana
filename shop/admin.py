from django.contrib import admin

from . import models


class ProductImagesInLine(admin.TabularInline):
    model = models.ProductImage
    fields = ['image',]
    extra = 1

class CommentsInLine(admin.TabularInline):
    model = models.CommentProduct
    fields = ['text','author','stars','active']
    extra = 1

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']
    
    inlines = [
        CommentsInLine,
        ProductImagesInLine,
    ]

@admin.register(models.CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    list_display = ['author','product','text','stars','active']
    
@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product','image']    
    