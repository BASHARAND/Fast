# Generated by Django 2.1.2 on 2019-01-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0036_auto_20190103_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]