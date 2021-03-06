# Generated by Django 2.1.2 on 2018-11-08 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Get',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,max_length=1000, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,max_length=1000, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,max_length=1000, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=60)),
                ('Price', models.IntegerField(default=15)),
                ('image', models.ImageField(blank=True, upload_to=' Profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_num', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='table_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='men.Table'),
        ),
        migrations.AddField(
            model_name='get',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='men.Order'),
        ),
        migrations.AddField(
            model_name='get',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='men.Product'),
        ),
    ]
