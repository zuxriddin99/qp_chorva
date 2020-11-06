from django.contrib import admin
from collections import OrderedDict
# Register your models here.
from .models import *
from constance.admin import ConstanceAdmin, ConstanceForm, Config


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'show')
    search_fields = ('title', 'description')
    list_filter = ('title', 'show')


admin.site.register(AboutPage, AboutPageAdmin)


class OurAdvantageAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(OurAdvantage, OurAdvantageAdmin)


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(ContactPage, ContactPageAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'message', 'date',)
    search_fields = ('name', 'number', 'date')
    date_hierarchy = 'date'


admin.site.register(ContactUs, ContactUsAdmin)


class PartnerPageAmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(PartnerPage, PartnerPageAmin)

CONSTANCE_CONFIG = OrderedDict([
    ('SITE_NAME', ('My Title', 'Website title')),
    ('SITE_DESCRIPTION', ('', 'Website description')),
    ('THEME', ('light-blue', 'Website theme')),
])


class CustomConfigForm(ConstanceForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ... do stuff to make your settings form nice ...


class ConfigAdmin(ConstanceAdmin):
    change_list_form = CustomConfigForm
    change_list_template = 'admin/config/settings.html'


admin.site.unregister([Config])
admin.site.register([Config], ConfigAdmin)
