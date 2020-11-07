# Generated by Django 3.1.3 on 2020-11-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='catalog_image')),
                ('text_1', models.CharField(blank=True, max_length=100)),
                ('text_2', models.CharField(blank=True, max_length=100)),
                ('text_3', models.CharField(blank=True, max_length=100)),
                ('text_4', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'пост:каталог',
                'verbose_name_plural': 'посты:каталог',
            },
        ),
    ]