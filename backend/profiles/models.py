from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    skills = models.JSONField(default=list)  # e.g., ["AR automation", "credit control"]
    location = models.CharField(max_length=100, blank=True)
    expertise = models.CharField(max_length=100, blank=True)  # e.g., "Accounts Receivable"
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.email}'s Profile"