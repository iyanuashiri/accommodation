from django import forms
from django.contrib.auth.models import User

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import Profile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    mobile_number = PhoneNumberField(
        widget= PhoneNumberInternationalFallbackWidget(region='NG')
    )

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'picture', 'institution', 'NYSC_call_up_number', 'staff_code_number',
                  'mobile_number', 'state_of_service')
