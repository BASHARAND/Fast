# Generated by Django 2.1.2 on 2018-11-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0015_auto_20181124_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest',
            name='logo',
            field=models.FileField(blank=True, upload_to=' Profile_image'),
        ),
    ]
