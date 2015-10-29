from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from cdb.models import Contact

# Create your views here.
class ContactDetail(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.noew()
        return context

class ContactList(ListView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    prepopulated_fields = { "slug": ("first_name"), }

    def get_success_url(self):
        return reverse('all-contacts')


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'email', 'phone_number']


class ContactDelete(DeleteView):
    model = Contact
