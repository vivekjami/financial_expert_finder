from django.db import models

class Review(models.Model):
    reviewer = models.ForeignKey('users.User', related_name='reviews_given', on_delete=models.CASCADE)
    expert = models.ForeignKey('users.User', related_name='reviews_received', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.email} for {self.expert.email}"