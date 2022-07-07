from django.db import models
from authentication.models import User


class Contert(models.Model):
    title = models.CharField(verbose_name='Название',max_length=255)
    img = models.ImageField(verbose_name='Фото',upload_to='contert')
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
    
class FavoriteContert(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    contert = models.ForeignKey(Contert, verbose_name='Contert', on_delete=models.CASCADE)