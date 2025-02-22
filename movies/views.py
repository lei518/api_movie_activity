from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter  # ✅ Import this!
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # ✅ Add OrderingFilter for sorting
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    filterset_class = MovieFilter

    search_fields = ['title', 'director', 'genre']  # Custom search across multiple fields
    ordering_fields = ['rating', 'release_year']  # ✅ Enable sorting by rating and release_year
    ordering = ['-rating']  # Default sorting by highest rating first

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        """Return movies with a rating of 8.0 or higher"""
        top_movies = self.get_queryset().filter(rating__gte=8.0)
        serializer = self.get_serializer(top_movies, many=True)
        return Response(serializer.data)
