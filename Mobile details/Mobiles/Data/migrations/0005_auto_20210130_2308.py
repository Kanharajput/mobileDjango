# Generated by Django 3.0.8 on 2021-01-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0004_auto_20210130_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone_img',
            field=models.ImageField(height_field=400, upload_to='pics', width_field=400),
        ),
    ]