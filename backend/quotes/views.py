from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'business':
            raise PermissionDenied("Only businesses can create quotes.")
        serializer.save(business=self.request.user)

    def get_queryset(self):
        # Users see only their own quotes
        if self.request.user.role == 'business':
            return Quote.objects.filter(business=self.request.user)
        return Quote.objects.filter(expert=self.request.user)