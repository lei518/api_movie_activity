import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact')  # ✅ Case-insensitive exact match
    release_year = django_filters.NumberFilter(field_name='release_year')  # ✅ Ensure correct filtering

    class Meta:
        model = Movie
        fields = ['genre', 'release_year']
