from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from profiles.models import Profile
from django.db.models import Avg

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'business':
            raise PermissionDenied("Only businesses can leave reviews.")
        serializer.save(reviewer=self.request.user)
        # Update expert's average rating
        expert = serializer.validated_data['expert']
        avg_rating = Review.objects.filter(expert=expert).aggregate(Avg('rating'))['rating__avg']
        Profile.objects.filter(user=expert).update(rating=avg_rating or 0.0)

    def get_queryset(self):
        # Show reviews based on user role
        if self.request.user.role == 'business':
            return Review.objects.filter(reviewer=self.request.user)
        return Review.objects.filter(expert=self.request.user)