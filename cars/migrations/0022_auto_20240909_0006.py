# Generated by Django 3.0.7 on 2024-09-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_auto_20240909_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
