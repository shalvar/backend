
from django.db import models


class Place(models.Model):
    
    place = models.CharField(verbose_name='Концертный зал/Кинотеатр',max_length=255)
    
    def __str__(self):
        return self.place
    
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'  
    
    