from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

class MovieView(APIView):
def get(self, request):
movies = Movie.objects.all()
serializer = MovieSerializer(movies, many=True)
return Response(serializer.data)

def post(self, request):
serializer = MovieSerializer(data=request.data)
if serializer.is_valid():
serializer.save()
return Response(serializer.data, status=201)
return Response(serializer.errors, status=400)

class ReviewView(APIView):
def get(self, request):
reviews = Review.objects.all()
serializer = ReviewSerializer(reviews, many=True)
return Response(serializer.data)

def post(self, request):
serializer = ReviewSerializer(data=request.data)
if serializer.is_valid():
serializer.save()
return Response(serializer.data, status=201)
return Response(serializer.errors, status=400)
