
from rest_framework import serializers
from film.models import Film
from django.core.exceptions import ValidationError



class FilmSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Film
        fields = '__all__'
        
    def createDateVal(self, value):
        if value (r'^\d{4}$'):
            raise ValidationError(
                ('%(value)s is not an even number'),
             params={'value': value},
        )

