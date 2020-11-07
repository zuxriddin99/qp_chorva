from django.urls import path, include
from django.views.generic import TemplateView

from appmain.views import AboutCompanyView, ContactPageView, ContactUsView, PartnerPageViews, CatalogPageView

urlpatterns = [

    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('about/', AboutCompanyView.as_view(), name='about'),
    path('catalog/', CatalogPageView.as_view(template_name="catalog.html"), name='catalog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('partner/', PartnerPageViews.as_view(), name='partner'),
    path('connection/', ContactUsView.as_view(), name='contactus')
]
