# Generated by Django 2.0.6 on 2018-07-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0007_auto_20180705_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='landlord_name',
            field=models.CharField(default='Ayomide', max_length=50),
        ),
        migrations.AddField(
            model_name='apartment',
            name='landlord_number',
            field=models.CharField(default='07034366179', max_length=50),
        ),
    ]
