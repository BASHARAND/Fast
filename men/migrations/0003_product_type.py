# Generated by Django 2.1.2 on 2018-11-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0002_auto_20181109_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Type',
            field=models.IntegerField(default=1),
        ),
    ]
