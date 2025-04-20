from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@example.com', password='password', role='expert'
        )

    def test_create_profile(self):
        profile = Profile.objects.create(
            user=self.user,
            bio='Test bio',
            location='New York',
            expertise=['AR Automation'],
            skills=['Python'],
            experience_years=5
        )
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, 'Test bio')