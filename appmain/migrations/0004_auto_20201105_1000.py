# Generated by Django 3.1.3 on 2020-11-05 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0003_auto_20201105_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'contac us'},
        ),
        migrations.AlterField(
            model_name='contactus',
            name='number',
            field=models.IntegerField(default=998),
        ),
    ]