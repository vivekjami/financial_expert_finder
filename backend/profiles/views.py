from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Allow users to view all profiles, but edit only their own
        if self.action in ['update', 'partial_update', 'destroy']:
            return Profile.objects.filter(user=self.request.user)
        return Profile.objects.all()