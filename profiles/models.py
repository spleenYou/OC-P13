from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Represents a profile

    Attributes:
        user (obj): object user
        favorite_city (str): name of the favorite city
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        "Returns a string containing the username"
        return self.user.username
