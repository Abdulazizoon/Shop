# Generated by Django 4.0.6 on 2022-08-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]