# Generated by Django 4.0.6 on 2023-01-16 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_film_pagination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='pagination',
        ),
    ]
