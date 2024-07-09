# Generated by Django 5.0.6 on 2024-07-09 10:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_url_created_at_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]