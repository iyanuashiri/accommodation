from django import forms

from .models import Apartment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class ApartmentForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Apartment
        fields = ('title', 'picture', 'description', 'location', 'rent', 'number_of_rooms', 'house_type', 'duration', 'landlord_name', 'landlord_number')
