from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Apartment

# Create your views here.


class ApartmentList(LoginRequiredMixin, generic.ListView):
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

