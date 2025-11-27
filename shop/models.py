from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager,self).get_queryset().filter(active=True)
    
class Products(models.Model):
    
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    
    length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args={self.pk})


class CommentProduct(models.Model):
    PRODUCT_STARS = [
        ('1','very bad'),
        ('2','bad'),
        ('3','normal'),
        ('4','good'),
        ('5','perfect'),
    ]
    
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name='comments',
        )
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='comments',
        )
    
    text = models.TextField()
    active = models.BooleanField(default=False)
    stars = models.CharField(
        max_length=10, 
        choices=PRODUCT_STARS,
        )
    

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    # manager
    objects = models.Manager()
    comment_filter = ActiveManager()
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
    
