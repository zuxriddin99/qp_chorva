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
        verbose_name = 'Add post about page'
        verbose_name_plural = 'Add posts about page'
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class ContactPage(models.Model):
    """ post in contact page """
    text = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='contact-page', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Add post contact page'
        verbose_name_plural = 'Add posts contact page'
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class ContactUs(models.Model):
    name = models.CharField(max_length=200, verbose_name='name of sender')
    number = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'contact us'
        verbose_name_plural = 'contact us'

    def __str__(self):
        return self.name


# class PartnerPage(models.Model):
#     text = models.CharField(max_length=100,blank=True)
#     image =

