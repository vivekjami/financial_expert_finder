from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView, SearchExpertsView

urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('search/', SearchExpertsView.as_view(), name='search-experts'),
]