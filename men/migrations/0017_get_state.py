# Generated by Django 2.1.2 on 2018-12-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0016_auto_20181124_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='get',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
