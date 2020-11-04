# Generated by Django 3.1.3 on 2020-11-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcompany',
            name='img',
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='image',
            field=models.ImageField(blank=True, upload_to='about/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='image_background',
            field=models.ImageField(blank=True, upload_to='about/%Y/%m/%d'),
        ),
    ]