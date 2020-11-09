from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from .translations import *


class AboutPageAdmin(TranslationAdmin):
    list_display = ('title', 'show')
    search_fields = ('title', 'description')
    list_filter = ('title', 'show')


admin.site.register(AboutPage, AboutPageAdmin)


class OurAdvantageAdmin(TranslationAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(OurAdvantage, OurAdvantageAdmin)


class ContactPageAdmin(TranslationAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(ContactPage, ContactPageAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'message', 'date',)
    search_fields = ('name', 'number', 'date')
    date_hierarchy = 'date'


admin.site.register(ContactUs, ContactUsAdmin)


class PartnerPageAdmin(TranslationAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(PartnerPage, PartnerPageAdmin)


class CatalogPageAdmin(TranslationAdmin):
    list_display = ('title', 'text_1', 'text_2', 'text_3', 'text_4')
    search_fields = ('title', 'text_1', 'text_2', 'text_3', 'text_4')


admin.site.register(CatalogPage, CatalogPageAdmin)


class MenuAdmin(TranslationAdmin):
    list_display = ('name',)


admin.site.register(Menu, MenuAdmin)
