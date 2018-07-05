# Generated by Django 2.0.6 on 2018-06-30 15:48

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20180630_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('description', models.TextField(max_length=1000)),
                ('available', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=10)),
                ('rent', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('house_type', models.CharField(max_length=50)),
                ('duration', models.CharField(default='1 YEAR', max_length=50)),
                ('number_of_rooms', models.CharField(choices=[('on', 'One'), ('tw', 'Two'), ('th', 'Three'), ('fo', 'Four'), ('fi', 'Five')], default='on', max_length=2)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='accounts.LandLord')),
                ('renter', models.ManyToManyField(blank=True, related_name='rents', to='accounts.Tenant')),
            ],
            options={
                'verbose_name': 'apartment',
                'verbose_name_plural': 'apartments',
            },
        ),
    ]
