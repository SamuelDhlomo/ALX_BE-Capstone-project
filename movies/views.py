from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination # Import pagination
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter # Import your MovieFilter

class MoviePagination(PageNumberPagination):
    page_size = 10 # Set the number of movies per page

class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter] # Add DjangoFilterBackend
    filterset_class = MovieFilter # Specify the filter set for movies
    ordering_fields = ['title', 'release_date', 'rating_avg'] # Allow ordering
    ordering = ['title'] # Default ordering
    pagination_class = MoviePagination # Enable pagination for movies
