# Generated by Django 2.1.2 on 2018-12-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0029_auto_20181209_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Type',
            field=models.IntegerField(choices=[(1, 'FOOD'), (2, 'DRINKS'), (3, 'SWEETS')], max_length=3),
        ),
    ]
