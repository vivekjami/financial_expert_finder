from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews_given')
    expert = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.PositiveIntegerField()  # 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.expert.username}"