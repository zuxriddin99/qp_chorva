from django.contrib import admin

# Register your models here.
from .models import *


class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'show')
    search_fields = ('title', 'description')
    list_filter = ('title', 'show')


admin.site.register(AboutCompany, AboutCompanyAdmin)
