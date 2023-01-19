from django_filters import rest_framework as filters
from film.models import Film

class FilmFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class FilmFilter(filters.FilterSet):
    genre = FilmFilterInFilter(field_name='genre', lookup_expr='in')


    class Meta:
        model = Film    
        fields = ['genre']