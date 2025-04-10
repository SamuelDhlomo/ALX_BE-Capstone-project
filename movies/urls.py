from django.urls import path
from .views import MovieListView, ReviewListView, ReviewDetailView  # Make sure to import ReviewListView and ReviewDetailView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
