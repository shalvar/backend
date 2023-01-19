from rest_framework.viewsets import ModelViewSet
from film.serializers import FilmSerializer
from film.models import Film
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .service import FilmFilter
from django.utils import translation



class FilmPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 20
    

    
    

class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = FilmPagination
    filter_backends = [DjangoFilterBackend]
    filterest_class = FilmFilter
    

   
    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='add_films')
    def add_films(self, requset,):
        serializer = self.serializer_class(data=requset,)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Фильм добавлен'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='first decade')
    def get_Fdecade(self, films):
            films = Film.objects.filter( Q(createDate__startswith='200') | Q(createDate__endswith='10'))
            data = FilmSerializer(instance=films, many=True).data
            return Response(data)
        
    @action(methods=['GET'], detail=False, url_path='second decade')
    
    def get_Sdecade(self, films):
            films = Film.objects.filter( Q(createDate__startswith='201') | Q(createDate__endswith='20'))
            data = FilmSerializer(instance=films, many=True).data
            return Response(data)
        
    @action(methods=['GET'], detail=False, url_path='third decade')
    
    def get_Tdecade(self, films):
            films = Film.objects.filter( Q(createDate__startswith='202') | Q(createDate__endswith='30'))
            data = FilmSerializer(instance=films, many=True).data
            return Response(data)
        
def initial(self, request, *args, **kwargs ):
    language = kwargs.get('lang')
    translation.activate(language)
    super(FilmViewSet, self).initial(request, *args, **kwargs)
    

        
    
    
    
    
 
   