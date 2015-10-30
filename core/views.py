from django.http import *

from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import auth
from django.core.context_processors import csrf

from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from .models import Contact
from .forms import *


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    print args
    return render(request, 'login.html', args)


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return redirect('/')

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
