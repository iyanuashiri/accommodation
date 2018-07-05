from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from cloudinary.models import CloudinaryField


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = CloudinaryField('image', blank=True, null=True)
    institution = models.TextField(max_length=100, default='University of Ibadan')
    NYSC_call_up_number = models.CharField(max_length=50, default='12345')
    staff_code_number = models.CharField(max_length=50, default='12634')
    mobile_number = models.CharField(max_length=20, default='07034366179')
    state_of_service = models.TextField(max_length=20, default='Zamfara')

    class Meta:
        verbose_name_plural = 'profiles'

    def __str__(self):
        return '{0}\'s profile'.format(self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})

    def get_date_of_birth(self):
        return self.date_of_birth


