from django.db import models


# Create your models here.

class AboutPage(models.Model):
    """"  posts in about page """
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about_page', blank=True, verbose_name='image 1')
    image_background = models.ImageField(upload_to='about_page2', blank=True, verbose_name='image 2')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'пост: о компании'
        verbose_name_plural = 'посты:о компании'
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class OurAdvantage(models.Model):
    text = models.CharField(max_length=100)
    image_2 = models.ImageField(upload_to='about_page', verbose_name='main image')
    image = models.ImageField(upload_to='about_page', blank=True, verbose_name='image')

    class Meta:
        verbose_name = 'пост: наше преимущество'
        verbose_name_plural = 'посты:наши преимущества'

    def __str__(self):
        return self.text


class ContactPage(models.Model):
    """ post in contact page """
    text = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='contact-page', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'пост:контакт'
        verbose_name_plural = 'посты:контакты'
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class ContactUs(models.Model):
    name = models.CharField(max_length=200, verbose_name='name of sender')
    number = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'заявкы'

    def __str__(self):
        return self.name


class PartnerPage(models.Model):
    text = models.CharField(max_length=100, blank=True)
    image_background = models.ImageField(upload_to='partner_image')
    image = models.ImageField(upload_to='partner_image', blank=True)

    class Meta:
        verbose_name = "пост:партнёр"
        verbose_name_plural = "посты:партнёр"

    def __str__(self):
        return self.text
