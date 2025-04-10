from django.contrib import admin
from .models import Movie, Review  # Import your Movie and Review models

admin.site.register(Movie)
admin.site.register(Review)
