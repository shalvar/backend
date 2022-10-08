from django.db import models

class Main(models.Model):
    title = models.CharField(verbose_name='Название',max_length=255)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фото',upload_to='posters')

    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Постер'
        verbose_name_plural = 'Постеры'
    