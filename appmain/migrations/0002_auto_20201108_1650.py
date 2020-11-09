# Generated by Django 3.1.3 on 2020-11-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='title_uz',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_1_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_1_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_1_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_2_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_2_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_2_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_3_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_3_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_3_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_4_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_4_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='text_4_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='title_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='title_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='text_en',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='text_ru',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='text_uz',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='name_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ouradvantage',
            name='text_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ouradvantage',
            name='text_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ouradvantage',
            name='text_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerpage',
            name='text_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerpage',
            name='text_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerpage',
            name='text_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
