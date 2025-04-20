from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    expertise = models.JSONField(default=list)  # e.g., ["AR Automation", "Invoice Management"]
    skills = models.JSONField(default=list)  # e.g., ["Python", "Excel"]
    experience_years = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"