# Generated by Django 3.0.8 on 2021-01-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0002_auto_20210122_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='para1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='para2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='para3',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='para4',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='para5',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='para6',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='para7',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]