# Generated by Django 4.0.6 on 2023-01-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0017_alter_film_genre_historicalfilm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='createDate',
            field=models.IntegerField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='historicalfilm',
            name='createDate',
            field=models.IntegerField(verbose_name='Дата создания'),
        ),
    ]