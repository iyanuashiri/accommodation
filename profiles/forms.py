import datetime

from django import forms
from django.forms.widgets import SelectDateWidget
from django.utils import datetime_safe

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import Profile
from accounts.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email_address')


class ProfileForm(forms.ModelForm):
    mobile_number = PhoneNumberField(
        widget= PhoneNumberInternationalFallbackWidget(region='NG')
    )
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(datetime.date.today().year - 40, datetime.date.today().year)), initial=datetime_safe.date.today())

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'picture', 'institution', 'NYSC_call_up_number', 'state_code_number',
                  'mobile_number', 'state_of_service')
