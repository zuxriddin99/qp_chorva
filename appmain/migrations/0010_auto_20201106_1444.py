# Generated by Django 3.1.3 on 2020-11-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0009_auto_20201105_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouradvantage',
            name='image_2',
            field=models.ImageField(upload_to='about_page', verbose_name='main image'),
        ),
    ]