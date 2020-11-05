from django.urls import reverse
from django.views.generic import ListView, CreateView

from .forms import ContactUsFom
from .models import *


# Create your views here.

class AboutCompanyView(ListView):
    queryset = AboutPage.objects.filter(show=True)
    template_name = 'about.html'
    context_object_name = 'aboutpage'


class ContactPageView(ListView):
    queryset = ContactPage.objects.all()
    template_name = 'contact.html'
    context_object_name = 'contactpage'


class ContactUsView(CreateView):
    form_class = ContactUsFom
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')


class PartnerPageViews(ListView):
    queryset = PartnerPage.objects.all()
    template_name = 'partner.html'
    context_object_name = 'partnerpage'
