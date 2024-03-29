from django.urls import reverse_lazy
from django.views import generic

from .forms import TenantSignUpForm, LandLordSignUpForm

# Create your views here.


class TenantSignUpView(generic.CreateView):
    form_class = TenantSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profiles:edit')


class LandLordSignUpView(generic.CreateView):
    form_class = LandLordSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')
