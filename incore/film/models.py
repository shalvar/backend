from django.db import models
from place.models import Place
from timetable.models import Timetable
from genre.models import Genre
from simple_history.models import HistoricalRecords
from rest_framework import serializers



class Film(models.Model):
    
    title = models.CharField(u'Название',max_length=255)
    description = models.TextField(verbose_name=u'Описание')
    img = models.ImageField(verbose_name='Фото',upload_to='films')
    timetable = models.ManyToManyField(verbose_name='Расписание ',to=Timetable,related_name='timetables')
    genre = models.ManyToManyField(verbose_name='Жанр',to=Genre,related_name='genre')
    createDate = models.CharField(verbose_name='Дата создания',max_length=4,)
    place = models.ManyToManyField(verbose_name='Кинотеатр',to=Place,related_name='places')
    history = HistoricalRecords()
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'  

