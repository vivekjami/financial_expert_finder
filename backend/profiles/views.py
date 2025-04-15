from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import filters
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['bio', 'skills', 'location', 'expertise']