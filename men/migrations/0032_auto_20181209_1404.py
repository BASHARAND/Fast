# Generated by Django 2.1.2 on 2018-12-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0031_auto_20181209_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest',
            name='Language',
            field=models.IntegerField(choices=[(1, 'العربية'), (2, 'English'), (3, 'русский'), (4, 'Türkçe')]),
        ),
    ]
