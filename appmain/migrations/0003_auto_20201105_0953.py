# Generated by Django 3.1.3 on 2020-11-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0002_auto_20201105_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name of sender')),
                ('number', models.IntegerField(default=0)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'send request',
                'verbose_name_plural': 'send requests',
            },
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
    ]
