# Generated by Django 3.0.8 on 2020-07-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='year_released',
            field=models.DateField(blank=True, null=True),
        ),
    ]
