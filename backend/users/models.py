from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('business', 'Business'),
        ('expert', 'Expert'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='business')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email