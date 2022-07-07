
from rest_framework.viewsets import ModelViewSet
from contert.serializers import ContertSerializer, FavoriteContertSerializer
from contert.models import Contert, FavoriteContert
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class ContertViewSet(ModelViewSet):
    queryset = Contert.objects.all()
    serializer_class = ContertSerializer

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favorite')
    def toggle_favorite(self, request, pk=None):
        user = request.user
        try:
            contert = self.queryset.get(pk=pk)
        except Contert.DoesNotExist:
            raise NotFound('contert not found')
        try:
            fav_contert = FavoriteContert.objects.get(user=user, contert=contert)
            fav_contert.delete()
            return Response({'message': 'removed'})
        except FavoriteContert.DoesNotExist:
            FavoriteContert.objects.create(user=user, contert=contert)
            return Response({'message': 'added'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favorites')
    def get_favorites(self, request):
        user = request.user
        conterts = FavoriteContert.objects.filter(user=user)
        data = FavoriteContertSerializer(instance=conterts, many=True).data
        return Response(data)
