from django.db import models
from django.shortcuts import reverse

from django.utils.translation import gettext_lazy as _

class ServicesModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Service Title"))
    short_description = models.TextField(verbose_name=_("Short Description"))
    full_description = models.TextField(verbose_name=_("Full Description"))
    
    class Meta:
        verbose_name = _('Services')
        verbose_name_plural = _('Services')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service_detail', args={self.pk})

    