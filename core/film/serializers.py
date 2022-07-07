from dataclasses import field
from rest_framework import serializers
from film.models import FavoriteFilm, Film
from main.models import Main
from authentication.serializers import User, UserSerializer


class MainSerializerForFilm(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title',]
 
        
class FilmSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Film
        fields = '__all__'


class FavoriteFilmSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    film_data = FilmSerializer(source='film')

    class Meta:
        model = FavoriteFilm
        exclude = ['user', 'film']
