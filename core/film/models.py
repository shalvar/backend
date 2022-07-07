from django.db import models
from authentication.models import User



class Film(models.Model):
    title = models.CharField(verbose_name='Название',max_length=255)
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(verbose_name='Фото',upload_to='films')
    timetable = models.TimeField(verbose_name='Расписание сеансов')
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'  
    
class FavoriteFilm(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Film', on_delete=models.CASCADE)