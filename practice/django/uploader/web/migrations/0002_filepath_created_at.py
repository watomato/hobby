# Generated by Django 2.2.6 on 2020-12-11 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepath',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]