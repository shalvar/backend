# Generated by Django 4.0.6 on 2022-07-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_favoritefilm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='photo',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='film',
            name='timetable',
            field=models.TimeField(verbose_name='Расписание сеансов'),
        ),
    ]
