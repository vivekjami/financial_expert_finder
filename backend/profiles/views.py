from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Profile
from .serializers import ProfileSerializer

class SearchExpertsView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        location = request.query_params.get('location', '')
        expertise = request.query_params.get('expertise', '')

        profiles = Profile.objects.filter(user__role='expert')
        if query:
            profiles = profiles.filter(
                Q(bio__icontains=query) |
                Q(skills__contains=[query]) |
                Q(expertise__contains=[query])
            )
        if location:
            profiles = profiles.filter(location__icontains=location)
        if expertise:
            profiles = profiles.filter(expertise__contains=[expertise])

        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)