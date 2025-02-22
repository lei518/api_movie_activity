from .models import Movie

class MovieService:
    @staticmethod
    def get_all_movies():
        """Fetch all movies"""
        return Movie.objects.all()

    @staticmethod
    def get_top_rated_movies():
        """Fetch movies with a rating of 8.0 or higher"""
        return Movie.objects.filter(rating__gte=8.0)

    @staticmethod
    def filter_movies_by_genre(genre):
        """Filter movies by genre"""
        return Movie.objects.filter(genre__iexact=genre)

    @staticmethod
    def sort_movies_by_release_year(order="desc"):
        """Sort movies by release year (default: descending)"""
        if order == "asc":
            return Movie.objects.all().order_by("release_year")
        return Movie.objects.all().order_by("-release_year")
