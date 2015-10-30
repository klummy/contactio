from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'info', 'avatar']
