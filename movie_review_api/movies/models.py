from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings # Import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="movie_app_users_groups",
        related_query_name="movie_app_user_group",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="movie_app_users_permissions",
        related_query_name="movie_app_user_permission",
    )

    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for '{self.movie.title}' by {self.user.username} ({self.rating}/5)"
