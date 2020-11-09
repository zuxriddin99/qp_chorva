from modeltranslation.translator import translator, TranslationOptions
from .models import AboutPage, OurAdvantage, ContactPage, PartnerPage, CatalogPage, Menu
from django.utils.translation import gettext_lazy as _
from qp_chorva.myconstanse import *


class AboutPageTranslationOption(TranslationOptions):
    fields = ('title', 'description')


translator.register(AboutPage, AboutPageTranslationOption)


class OurAdvantageTranslationOption(TranslationOptions):
    fields = ('text',)


translator.register(OurAdvantage, OurAdvantageTranslationOption)


class ContactPageTranslationOption(TranslationOptions):
    fields = ('text',)


translator.register(ContactPage, ContactPageTranslationOption)


class PartnerPageTranslationOption(TranslationOptions):
    fields = ('text',)


translator.register(PartnerPage, PartnerPageTranslationOption)


class CatalogPageTranslationOption(TranslationOptions):
    fields = ('title', 'text_1', 'text_2', 'text_3', 'text_4',)


translator.register(CatalogPage, CatalogPageTranslationOption)


class MenuTranslationOption(TranslationOptions):
    fields = ('name',)


translator.register(Menu, MenuTranslationOption)


# class CONSTANCE_CONFIGTranslationOption(TranslationOptions):
#     fields = ('TITLE_INDEX',)
#
#
# translator.register(CONSTANCE_CONFIG, CONSTANCE_CONFIGTranslationOption)
