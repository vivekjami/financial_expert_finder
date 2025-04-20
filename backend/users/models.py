from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[('business', 'Business'), ('expert', 'Expert')],
        default='business'
    )

    def __str__(self):
        return self.email