from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager,self).get_queryset().filter(active=True)


class Products(models.Model):
    
    title = models.CharField(max_length=100, verbose_name=_('title'))
    short_description = models.CharField(max_length=300, verbose_name=_('short description'))
    full_description = models.TextField(verbose_name=_('full description'))
    
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    
    length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name=_('length'))
    width = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name=_('width'))
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name=_('height'))
    
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime modified'))
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class CommentProduct(models.Model):
    PRODUCT_STARS = [
        ('1',_('very bad')),
        ('2',_('bad')),
        ('3',_('normal')),
        ('4',_('good')),
        ('5',_('perfect')),
    ]
    
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name=_('product'),
        )
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name=_('author'),
        )
    
    text = models.TextField(verbose_name=_('text'))
    active = models.BooleanField(default=False, verbose_name=_('active'),)
    stars = models.CharField(
        max_length=1, 
        choices=PRODUCT_STARS,
        verbose_name=_('stars'),
        )
    

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime created'),)
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime modified'),)
    
    # manager
    objects = models.Manager()
    comment_filter = ActiveManager()
    
    class Meta:
        verbose_name = _('CommentProduct')
        verbose_name_plural = _('CommentProducts')
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
     
class ProductImage(models.Model):
    
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name='images',
        verbose_name=_('product'),
        )
    image = models.ImageField(
        upload_to='product/product_cover', 
        blank=True, 
        verbose_name=_('image')
        )
    
    class Meta:
        verbose_name = _('ProductImage')
        verbose_name_plural = _('ProductImages')
    
    def __str__(self):
        return str(self.product)
    