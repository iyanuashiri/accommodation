from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tenant


class TenantSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email_address', 'fullname', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_tenant = True

        if commit:
            user.save()
            Tenant.objects.create(user=user)
            user.save()
        return user


