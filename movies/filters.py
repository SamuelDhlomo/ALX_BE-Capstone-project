import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    genre = django_filters.CharFilter(lookup_expr='iexact', label='Genre is')
    release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year', label='Release Year')
    min_rating = django_filters.NumberFilter(field_name='rating_avg', lookup_expr='gte', label='Minimum Average Rating')
    max_rating = django_filters.NumberFilter(field_name='rating_avg', lookup_expr='lte', label='Maximum Average Rating')

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year', 'min_rating', 'max_rating']
