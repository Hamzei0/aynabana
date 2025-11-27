from django.db import models
from django.shortcuts import reverse


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

