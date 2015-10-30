from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, DeleteView


from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactListView(ListView):
    template_name = 'contact_list.html'
    model = Contact
    context_object_name = 'contacts'

class CreateContactView(CreateView):
    model = Contact
    fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'info']

def contact_list(request):
    contacts = Contact.objects.filter(date_added__lte=timezone.now()).order_by('date_added')
    return render(request, 'core/contact_list.html', {'contacts': contacts})


def contact_new(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            # contact.published_date = timezone.now()
            contact.save()
            return redirect('/', pk=contact.pk)
    else:
        form = ContactForm()

    return render(request, 'core/contact_form_edit.html', {'form': form})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            # contact.published_date = timezone.now()
            contact.save()
            return redirect('/', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'core/contact_form_edit.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('/', pk=contact.pk)
