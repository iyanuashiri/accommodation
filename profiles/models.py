from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = CloudinaryField('image', blank=True, null=True)
    institution = models.CharField(max_length=100)
    NYSC_call_up_number = models.CharField(max_length=50)
    staff_code_number = models.CharField(max_length=50)
    mobile_number = PhoneNumberField()
    state_of_service = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'profiles'

    def __str__(self):
        return '{0}\'s profile'.format(self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.pk})

    def get_date_of_birth(self):
        return self.date_of_birth


