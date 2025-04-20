from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from profiles.models import Profile
import random

class Command(BaseCommand):
    help = 'Populates the database with authentic user data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        expertise_options = [
            'AR Automation', 'Invoice Management', 'Credit Control', 'Payment Processing', 'Financial Analysis'
        ]
        skills_options = ['Python', 'Excel', 'SQL', 'QuickBooks', 'SAP']
        locations = ['New York', 'London', 'San Francisco', 'Toronto', 'Sydney']

        # Create 25 business users
        for i in range(25):
            user = User.objects.create_user(
                username=f'business{i+1}',
                email=f'business{i+1}@example.com',
                password='password123',
                role='business'
            )
            Profile.objects.create(
                user=user,
                bio=f'Business {i+1} specializing in financial services.',
                location=random.choice(locations),
            )

        # Create 25 expert users
        for i in range(25):
            user = User.objects.create_user(
                username=f'expert{i+1}',
                email=f'expert{i+1}@example.com',
                password='password123',
                role='expert'
            )
            Profile.objects.create(
                user=user,
                bio=f'Expert {i+1} with experience in AR solutions.',
                location=random.choice(locations),
                expertise=random.sample(expertise_options, k=2),
                skills=random.sample(skills_options, k=3),
                experience_years=random.randint(1, 15),
                rating=round(random.uniform(3.0, 5.0), 1)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated 50 users'))