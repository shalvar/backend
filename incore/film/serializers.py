from dataclasses import field
from rest_framework import serializers
from film.models import Film
from createDate.models import CreateDate



class FilmSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Film
        fields = '__all__'

