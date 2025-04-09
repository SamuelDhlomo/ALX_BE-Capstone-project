from rest_framework.views import APIView
from django.urls import path
from .views import MovieListView, ReviewListView, RootView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('', RootView.as_view(), name='root'),
]
