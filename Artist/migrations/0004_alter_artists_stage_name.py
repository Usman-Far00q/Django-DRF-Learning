# Generated by Django 4.1.7 on 2023-03-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0003_alter_artists_first_name_alter_artists_stage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='stage_name',
            field=models.CharField(default='temp_val', max_length=30),
            preserve_default=False,
        ),
    ]
