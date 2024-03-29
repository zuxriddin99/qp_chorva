from django.urls import reverse
from django.views.generic import ListView, CreateView

from .forms import ContactUsFom
from .models import *
from django.shortcuts import render
from constance import config


# Create your views here.

class AboutCompanyView(ListView):
    queryset = AboutPage.objects.filter(show=True)
    template_name = 'about.html'
    context_object_name = 'aboutpage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advantage'] = OurAdvantage.objects.all()

        # And so on for more models
        return context


class ContactPageView(ListView):
    queryset = ContactPage.objects.all()
    template_name = 'contact.html'
    context_object_name = 'contactpage'


class CatalogPageView(ListView):
    queryset = CatalogPage.objects.all()
    template_name = 'catalog.html'
    context_object_name = 'catalogpage'


class ContactUsView(CreateView):
    form_class = ContactUsFom
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')


class PartnerPageViews(ListView):
    queryset = PartnerPage.objects.all()
    template_name = 'partner.html'
    context_object_name = 'partnerpage'

# def myview(request):
#     return render(request, 'about.html', {'config': config})

