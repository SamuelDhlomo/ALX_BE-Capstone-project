from django.urls import path
from .views import MovieListView, ReviewListView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
]
