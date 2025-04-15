from rest_framework import serializers
from .models import Quote
from users.serializers import UserSerializer

class QuoteSerializer(serializers.ModelSerializer):
    business = UserSerializer(read_only=True)
    expert = UserSerializer(read_only=True)
    class Meta:
        model = Quote
        fields = ['id', 'business', 'expert', 'description', 'status', 'created_at']