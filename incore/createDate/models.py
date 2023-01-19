from django.db import models

class CreateDate(models.Model):
    date = models.CharField(verbose_name='Дата выхода',max_length=4)
    
    def __str__(self):
        return self.date
    
    class Meta:
        verbose_name = 'Дата выхода'
        verbose_name_plural = 'Дата выхода'
