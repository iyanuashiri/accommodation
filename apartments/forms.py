from django import forms

from .models import Apartment


class ApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = ('title', 'picture', 'description', 'location', 'rent', 'number_of_rooms', 'house_type', 'duration')
