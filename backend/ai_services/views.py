from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatbotSerializer, MatchSerializer
from profiles.models import Profile
from .services import match_experts
import openai
from django.conf import settings

class ChatbotView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ChatbotSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            try:
                openai.api_key = settings.OPENAI_API_KEY
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}]
                )
                return Response({'reply': response.choices[0].message.content})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchExpertsView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            description = serializer.validated_data['description']
            profiles = Profile.objects.all().values('id', 'bio', 'skills')
            matches = match_experts(description, list(profiles))
            return Response({'matches': matches})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)