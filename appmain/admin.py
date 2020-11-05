from django.contrib import admin

# Register your models here.
from .models import *


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'show')
    search_fields = ('title', 'description')
    list_filter = ('title', 'show')


admin.site.register(AboutPage, AboutPageAdmin)


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(ContactPage, ContactPageAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'message', 'date',)
    search_fields = ('name', 'number', 'date')
    date_hierarchy = 'date'


admin.site.register(ContactUs, ContactUsAdmin)
