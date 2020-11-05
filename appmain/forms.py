from django.contrib.contenttypes import forms

from .models import ContactUs


class ContactUsFom(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'number', 'message')
