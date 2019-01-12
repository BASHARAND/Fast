# Generated by Django 2.1.2 on 2018-12-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0022_langru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lang',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='langen',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='langru',
            name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='descriptionar',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='descriptionru',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='namear',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nameru',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='Lang',
        ),
        migrations.DeleteModel(
            name='Langen',
        ),
        migrations.DeleteModel(
            name='Langru',
        ),
    ]
