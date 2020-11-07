from django.contrib import admin
from .models import *


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


class CatalogPageAmin(admin.ModelAdmin):
    list_display = ('title', 'text_1', 'text_2', 'text_3', 'text_4')
    search_fields = ('title', 'text_1', 'text_2', 'text_3', 'text_4')


admin.site.register(CatalogPage, CatalogPageAmin)

admin.site.register(Menu)