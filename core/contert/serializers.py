from rest_framework import serializers
from contert.models import FavoriteContert, Contert
from main.models import Main
from authentication.serializers import User, UserSerializer

class MainSerializerForContert(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title',]


class ContertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contert
        fields = '__all__'


class FavoriteContertSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    contert_data = ContertSerializer(source='contert')

    class Meta:
        model = FavoriteContert
        exclude = ['user', 'contert']
       