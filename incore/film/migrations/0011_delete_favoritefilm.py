# Generated by Django 4.0.6 on 2023-01-18 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0010_remove_film_createdate_film_createdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteFilm',
        ),
    ]
