from django.db import models
from django.shortcuts import reverse

from cloudinary.models import CloudinaryField

from accounts.models import Tenant

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = CloudinaryField('image', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'profiles'

    def __str__(self):
        return '{0}\'s profile'.format(self.user.fullname)

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})

    def get_date_of_birth(self):
        return self.date_of_birth


