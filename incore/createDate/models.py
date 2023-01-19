from django.db import models

class CreateDate(models.Model):
    date = models.IntegerField(verbose_name='Дата выхода')
    
    def __str__(self):
        return self.date
    
    class Meta:
        verbose_name = 'Дата выхода'
        verbose_name_plural = 'Дата выхода'
