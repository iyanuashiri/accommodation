# Generated by Django 2.0.6 on 2018-07-02 17:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20180702_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='sample.jpg', max_length=255, verbose_name='image'),
        ),
    ]
