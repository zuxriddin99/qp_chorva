from django.db import models


# Create your models here.

class AboutCompany(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/%Y/%m/%d', blank=True)
    image_background = models.ImageField(upload_to='about/%Y/%m/%d', blank=True)
    show = models.BooleanField(default=True)
