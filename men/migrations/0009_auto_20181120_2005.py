# Generated by Django 2.1.2 on 2018-11-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0008_auto_20181120_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
