# Generated by Django 4.1.7 on 2023-03-06 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0005_alter_artists_first_name_alter_artists_stage_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artists',
            options={'verbose_name_plural': 'artists'},
        ),
    ]
