from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
