from django.contrib import admin

from . import models

class CommentsInLine(admin.TabularInline):
    model = models.CommentProduct
    fields = ['text','author','stars','active']
    extra = 1

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']
    
    inlines = [
        CommentsInLine,
    ]

@admin.register(models.CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    list_display = ['author','product','text','active','stars']
    