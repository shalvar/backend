# Generated by Django 4.0.6 on 2022-07-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0003_rename_photo_concert_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='img',
            field=models.ImageField(upload_to='concerts', verbose_name='Фото'),
        ),
    ]