# Generated by Django 2.1.2 on 2018-12-05 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0018_lang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lang',
            old_name='description',
            new_name='ardescription',
        ),
        migrations.RenameField(
            model_name='lang',
            old_name='name',
            new_name='arname',
        ),
    ]
