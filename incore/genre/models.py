from django.db import models

class Genre(models.Model):
    
    title = models.CharField(verbose_name='Название',max_length=255)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'