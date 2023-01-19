from django.db import models
from authentication.models import User
from place.models import Place
from timetable.models import Timetable
from createDate.models import CreateDate
from genre.models import Genre


class Concert(models.Model):
    title = models.CharField(verbose_name='Название',max_length=255)
    img = models.ImageField(verbose_name='Фото',upload_to='concerts')
    timetable = models.ManyToManyField(verbose_name='Расписание ',to=Timetable,related_name='timetablesForConterts')
    genre = models.ManyToManyField(verbose_name='Жанр',to=Genre,related_name='genresForConterts')
    createDate = models.CharField(verbose_name='Дата создания',max_length=4)
    place = models.ManyToManyField(verbose_name='Концертный зал',to=Place,related_name='placesForConterts')
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
    
class FavoriteConcert(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, verbose_name='Concert', on_delete=models.CASCADE)