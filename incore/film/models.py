from django.db import models
from authentication.models import User
from place.models import Place
from timetable.models import Timetable



class Film(models.Model):
    title = models.CharField(verbose_name='Название',max_length=255)
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(verbose_name='Фото',upload_to='films')
    timetable = models.ManyToManyField(verbose_name='Расписание ',to=Timetable,related_name='timetables')
    place = models.ManyToManyField(verbose_name='Кинотеатр',to=Place,related_name='places')
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'  
    
class FavoriteFilm(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Film', on_delete=models.CASCADE)