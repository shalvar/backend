from rest_framework import serializers
from concert.models import FavoriteConcert, Concert
from main.models import Main
from authentication.serializers import User, UserSerializer

class MainSerializerForConcert(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title',]


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = '__all__'


class FavoriteConcertSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    concert_data = ConcertSerializer(source='concert')

    class Meta:
        model = FavoriteConcert
        exclude = ['user', 'concert']
       