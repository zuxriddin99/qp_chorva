from django.db import models

# Create your models here.
from django.urls import reverse


class AboutPage(models.Model):
    """" first articles in about page """
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about_page', blank=True, verbose_name='image 1')
    image_background = models.ImageField(upload_to='about_page2', blank=True, verbose_name='image 2')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'статья: о компании'
        verbose_name_plural = 'статьи:о компании'
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class OurAdvantage(models.Model):
    """" second articles in about page """
    text = models.CharField(max_length=100)
    image_2 = models.ImageField(upload_to='about_page', verbose_name='main image')
    image = models.ImageField(upload_to='about_page', blank=True, verbose_name='image')

    class Meta:
        verbose_name = 'статья: наше преимущество'
        verbose_name_plural = 'статьи:наши преимущества'

    def __str__(self):
        return self.text


class ContactPage(models.Model):
    """ articles in contact page """
    text = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='contact-page', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'статья:контакт'
        verbose_name_plural = 'статьи:контакты'
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class ContactUs(models.Model):
    """ contact with company via forma"""
    name = models.CharField(max_length=200, verbose_name='имя отправителя сообщения')
    number = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'заявкы'

    def __str__(self):
        return self.name


class PartnerPage(models.Model):
    """articles in partner page"""
    text = models.CharField(max_length=100, blank=True)
    image_background = models.ImageField(upload_to='partner_image')
    image = models.ImageField(upload_to='partner_image', blank=True)

    class Meta:
        verbose_name = "статья:партнёр"
        verbose_name_plural = "статьи:партнёр"

    def __str__(self):
        return self.text


class CatalogPage(models.Model):
    """articles in catalog page"""
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='catalog_image')
    text_1 = models.CharField(max_length=100, blank=True)
    text_2 = models.CharField(max_length=100, blank=True)
    text_3 = models.CharField(max_length=100, blank=True)
    text_4 = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "статья:каталог"
        verbose_name_plural = "статьи:каталог"

    def __str__(self):
        return self.title


class Menu(models.Model):
    """ for menu"""
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def get_absolute_url(self):
        return reverse(self.url)

    def __str__(self):
        return self.name
