from django.db import models
from django.shortcuts import reverse

class ServicesModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Service Title")
    short_description = models.TextField(verbose_name="Short Description")
    full_description = models.TextField(verbose_name="Full Description")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service_detail', args={self.pk})

    