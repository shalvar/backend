
from django.db import models

class Timetable(models.Model):
    time = models.TimeField(verbose_name='Время')
    
    def __str__(self):
        return self.time.strftime('%H:%M')
    
    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'
       