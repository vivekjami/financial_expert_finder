from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get('message')
        if not message:
            return Response({'error': 'Message is required'}, status=400)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for the Financial Expert Finder platform, specializing in accounts receivable."},
                    {"role": "user", "content": message},
                ]
            )
            return Response({'response': response.choices[0].message.content})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sentence_transformers import SentenceTransformer, util
from profiles.models import Profile
from profiles.serializers import ProfileSerializer

class ExpertMatchingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        business_description = request.data.get('description')
        if not business_description:
            return Response({'error': 'Description is required'}, status=400)

        model = SentenceTransformer('all-MiniLM-L6-v2')
        business_embedding = model.encode(business_description, convert_to_tensor=True)

        profiles = Profile.objects.filter(user__role='expert')
        matches = []
        for profile in profiles:
            expertise_text = ' '.join(profile.expertise + profile.skills + [profile.bio])
            profile_embedding = model.encode(expertise_text, convert_to_tensor=True)
            similarity = util.cos_sim(business_embedding, profile_embedding).item()
            matches.append({'profile': ProfileSerializer(profile).data, 'similarity': similarity})

        matches = sorted(matches, key=lambda x: x['similarity'], reverse=True)[:5]
        return Response({'matches': matches})