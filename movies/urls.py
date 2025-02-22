from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet  # ✅ Import the ViewSet

# Create a router for ViewSet-based routes
router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")  # ✅ Register ViewSet

urlpatterns = [
    path("", include(router.urls)),  # ✅ Use DRF's router for ViewSets
]
