from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'articles'

urlpatterns = [

    path('', TemplateView.as_view(template_name="base.html"), name='main'),
]
