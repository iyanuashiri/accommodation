from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from cloudinary.models import CloudinaryField

from accounts.models import Tenant, LandLord

# Create your models here.


class Apartment(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    picture = CloudinaryField('image', blank=True)
    description = models.TextField(max_length=1000)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=10)
    tenants = models.ManyToManyField(Tenant, related_name='rents', blank=True)
    created_by = models.ForeignKey(LandLord, on_delete=models.CASCADE, related_name='apartments')

    class Meta:
        verbose_name_plural = 'apartments'
        verbose_name = 'apartment'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('apartments:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Apartment, self).save(*args, **kwargs)
