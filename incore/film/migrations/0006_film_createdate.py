# Generated by Django 4.0.6 on 2023-01-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createDate', '0001_initial'),
        ('film', '0005_alter_film_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='createDate',
            field=models.ManyToManyField(related_name='createDates', to='createDate.createdate', verbose_name='Дата создания'),
        ),
    ]