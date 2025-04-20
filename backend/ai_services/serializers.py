from rest_framework import serializers

class ChatbotSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)
    reply = serializers.CharField(max_length=1000, read_only=True)

class MatchSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=1000)