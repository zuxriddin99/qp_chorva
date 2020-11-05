from urllib import request

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.contrib import messages

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


# def connection_view(request):
#     if request.method == 'POST':
#         form = ConnectionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.INFO, 'Message Submitted.')
#             return redirect('connection_view')
#     else:
#         form = ConnectionForm()
#     return render(request, 'contact.html', {'form': form})

class ContactUsView(SuccessMessageMixin, CreateView):
    form_class = ContactUsFom
    template_name = 'contact.html'

    def get_success_url(self):
        # messages.success(request, 'Your profile is updated successfully!')
        return reverse('contact')

    success_message = 'salom'
