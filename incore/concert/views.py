
from rest_framework.viewsets import ModelViewSet
from concert.serializers import ConcertSerializer, FavoriteConcertSerializer
from concert.models import Concert, FavoriteConcert
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class ConcertViewSet(ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favorite')
    def toggle_favorite(self, request, pk=None):
        user = request.user
        try:
            concert = self.queryset.get(pk=pk)
        except Concert.DoesNotExist:
            raise NotFound('concert not found')
        try:
            fav_concert = FavoriteConcert.objects.get(user=user, concert=concert)
            fav_concert.delete()
            return Response({'message': 'removed'})
        except FavoriteConcert.DoesNotExist:
            FavoriteConcert.objects.create(user=user, concert=concert)
            return Response({'message': 'added'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favorites')
    def get_favorites(self, request):
        user = request.user
        concerts = FavoriteConcert.objects.filter(user=user)
        data = FavoriteConcertSerializer(instance=concerts, many=True).data
        return Response(data)
