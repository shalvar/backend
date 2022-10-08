from rest_framework.viewsets import ModelViewSet
from film.serializers import FilmSerializer, FavoriteFilmSerializer
from film.models import Film, FavoriteFilm
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='film')
    def get_favorites(self, request):
        user = request.user
        films = Film.objects.filter(user=user)
        data = FilmSerializer(instance=films, many=True).data
        return Response(data)    

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favorite')
    def toggle_favorite(self, request, pk=None):
        user = request.user
        try:
            film = self.queryset.get(pk=pk)
        except Film.DoesNotExist:
            raise NotFound('film not found')
        try:
            fav_film = FavoriteFilm.objects.get(user=user, film=film)
            fav_film.delete()
            return Response({'message': 'removed'})
        except FavoriteFilm.DoesNotExist:
            FavoriteFilm.objects.create(user=user, film=film)
            return Response({'message': 'added'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favorites')
    def get_favorites(self, request):
        user = request.user
        films = FavoriteFilm.objects.filter(user=user)
        data = FavoriteFilmSerializer(instance=films, many=True).data
        return Response(data)