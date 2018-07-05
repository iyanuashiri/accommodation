# Generated by Django 2.0.6 on 2018-07-02 17:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_auto_20180702_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
