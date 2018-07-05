from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mass_mail
from django.contrib import messages

from accounts.models import User
from .models import Apartment

# Create your views here.


class ApartmentList(generic.ListView):
    model = Apartment
    template_name = 'apartments/apartment_list.html'
    context_object_name = 'apartments'
    paginate_by = 50
    queryset = Apartment.objects.all()


class ApartmentDetail(LoginRequiredMixin, generic.DetailView):
    model = Apartment
    template_name = 'apartments/apartment_detail.html'
    context_object_name = 'apartment'


class ApartmentFormMixin(object):
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ApartmentCreate(LoginRequiredMixin, SuccessMessageMixin, ApartmentFormMixin, generic.CreateView):
    model = Apartment
    template_name = 'apartments/apartment_form.html'
    fields = ('title', 'picture', 'description', 'location', 'rent', 'number_of_rooms', 'house_type', 'duration')
    success_message = "%(title)s was updated successfully"


class ApartmentUpdate(LoginRequiredMixin, SuccessMessageMixin, ApartmentFormMixin, generic.UpdateView):
    model = Apartment
    template_name = 'apartments/apartment_update.html'
    fields = ('title', 'picture', 'description', 'location', 'rent', 'number_of_rooms', 'house_type', 'duration')
    success_message = "%(title)s was updated successfully"


class ApartmentDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Apartment
    template_name = 'apartments/apartment_confirm_delete.html'
    success_url = reverse_lazy('apartments:delete')
    success_message = "%(title)s was updated successfully"


@login_required()
def request_contact(request, apartment_id):
    apartment = get_object_or_404(Apartment, apartment_id)
    tenant = User.objects.get(email_address=request.user.email_address)
    message_to_tenant = ('Request Received', 'Congratulations {}, one of our agents will contact shortly'.format(tenant.first_name, 'dont-reply@example.com', '{}'.format(tenant.email_address)))
    message_to_agent = ('Request for contact', '{0} is interested in {1}. His mobile number is {2}'.format(tenant.get_full_name(), apartment.title, tenant.profile.mobile_number), 'ayo@example.com', 'ayo@gmail.com')
    send_mass_mail((message_to_tenant, message_to_agent), fail_silently=False)
    messages.success(request, 'Congratulations, one of our agents will contact shortly')
    return redirect('apartments:detail', pk=apartment.pk)

