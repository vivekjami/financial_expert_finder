
from rest_framework import serializers
from .models import Profile
from users.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'skills', 'location', 'expertise', 'rating']
        read_only_fields = ['id', 'rating']