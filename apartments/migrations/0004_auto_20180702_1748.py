# Generated by Django 2.0.6 on 2018-07-02 17:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_auto_20180702_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/iyanuashiri/image/upload/v1525737213/sample.jpg', max_length=255, verbose_name='image'),
        ),
    ]