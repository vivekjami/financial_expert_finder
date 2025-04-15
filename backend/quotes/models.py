from django.db import models

class Quote(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    business = models.ForeignKey('users.User', related_name='quotes_sent', on_delete=models.CASCADE)
    expert = models.ForeignKey('users.User', related_name='quotes_received', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote from {self.business.email} to {self.expert.email}"