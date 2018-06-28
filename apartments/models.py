from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from cloudinary.models import CloudinaryField

from accounts.models import Tenant, LandLord

# Create your models here.


class Apartment(models.Model):

    ONE = 'on'
    TWO = 'tw'
    THREE = 'th'
    FOUR = 'fo'
    FIVE = 'fi'

    NUMBER_OF_ROOMS = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    picture = CloudinaryField('image', blank=True)
    description = models.TextField(max_length=1000)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=10)
    renter = models.ManyToManyField(Tenant, related_name='rents', blank=True)
    created_by = models.ForeignKey(LandLord, on_delete=models.CASCADE, related_name='apartments')
    rent = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    house_type = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, default='1 YEAR')
    number_of_rooms = models.CharField(max_length=2, choices=NUMBER_OF_ROOMS, default=ONE)

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
