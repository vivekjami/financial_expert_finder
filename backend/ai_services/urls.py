from django.urls import path
from .views import ChatbotView, ExpertMatchingView

urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('match/', ExpertMatchingView.as_view(), name='expert-matching'),
]