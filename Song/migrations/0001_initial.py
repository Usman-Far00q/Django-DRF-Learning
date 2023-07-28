# Generated by Django 4.1.7 on 2023-07-28 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artist', '0007_alter_artists_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rating', models.IntegerField(default=5.0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('sung_by_artists', models.ManyToManyField(null=True, related_name='sang_songs', to='Artist.artists')),
            ],
            options={
                'db_table': 'Songs',
            },
        ),
    ]