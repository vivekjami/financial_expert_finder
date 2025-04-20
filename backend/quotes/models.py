from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Quote(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    business = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='quotes_sent')
    expert = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='quotes_received')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote from {self.business.username} to {self.expert.username}"