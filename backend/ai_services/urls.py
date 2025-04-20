from django.urls import path
from .views import ChatbotView, MatchExpertsView

urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('match/', MatchExpertsView.as_view(), name='match-experts'),
]