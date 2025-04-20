from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.JSONField()  # e.g., ["AR automation", "credit control"]
    location = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.email}'s Profile"