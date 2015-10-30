from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from .models import Contact

# Create your views here.
class ContactListView(ListView):
    template_name = 'core/contact_list.html'
    model = Contact
    context_object_name = 'contacts'
