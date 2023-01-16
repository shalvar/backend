from django.db import models
from authentication.models import User
from place.models import Place
from timetable.models import Timetable


class Concert(models.Model):
    title = models.CharField(verbose_name='Название',max_length=255)
    img = models.ImageField(verbose_name='Фото',upload_to='concerts')
   
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
    
class FavoriteConcert(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, verbose_name='Concert', on_delete=models.CASCADE)