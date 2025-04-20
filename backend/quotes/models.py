from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Quote(models.Model):
    business = models.ForeignKey(User, related_name='quotes_sent', on_delete=models.CASCADE)
    expert = models.ForeignKey(User, related_name='quotes_received', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote from {self.business.email} to {self.expert.email}"