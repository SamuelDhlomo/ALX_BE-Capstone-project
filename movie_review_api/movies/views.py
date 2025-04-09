from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'release_date']
    ordering = ['title']

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at', 'movie__title']
    ordering = ['-created_at']

class RootView(APIView):
    """
    A simple view to show the available API endpoints.
    """
    def get(self, request, *args, **kwargs):
        return Response({
            'movies': request.build_absolute_uri('movies/'),
            'reviews': request.build_absolute_uri('reviews/'),
            
        })
