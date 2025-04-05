from django.urls import path
from .views import MovieView, ReviewView

urlpatterns = [
path('movies/', MovieView.as_view()),
path('reviews/', ReviewView.as_view()),
]
