# Generated by Django 2.2.6 on 2020-11-22 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20201122_2253'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WebDocument',
            new_name='Document',
        ),
    ]