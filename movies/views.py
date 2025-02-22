from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter
from .services import MovieService  # ✅ Import the service layer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieService.get_all_movies()  # ✅ Use service layer
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = MovieFilter

    search_fields = ["title", "director", "genre"]
    ordering_fields = ["rating", "release_year"]
    ordering = ["-rating"]

    @action(detail=False, methods=["get"])
    def top_rated(self, request):
        """Return top-rated movies"""
        top_movies = MovieService.get_top_rated_movies()  # ✅ Use service layer
        serializer = self.get_serializer(top_movies, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def sort_by_release_year(self, request):
        """Sort movies by release year (asc or desc)"""
        order = request.query_params.get("order", "desc")  # Get order from query params
        sorted_movies = MovieService.sort_movies_by_release_year(order)  # ✅ Use service layer
        serializer = self.get_serializer(sorted_movies, many=True)
        return Response(serializer.data)
