# Generated by Django 2.1.2 on 2018-11-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0011_table_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your Resturant Name Here', max_length=50)),
                ('phone', models.CharField(default='02-555111222', max_length=15)),
                ('address', models.TextField(default='Address Here', max_length=40)),
                ('logo', models.ImageField(blank=True, upload_to=' Profile_image')),
            ],
        ),
    ]