# Generated by Django 4.0.6 on 2023-01-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createDate', '0004_alter_createdate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createdate',
            name='date',
            field=models.CharField(max_length=4, verbose_name='Дата выхода'),
        ),
    ]
