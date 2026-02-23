from django.contrib.auth import get_user_model
from app.models import jobseeker, company
from django.db import transaction
import random

User = get_user_model()

@transaction.atomic
def create_fake_users():
    users = []

    # Create 25 Job Seekers
    for i in range(1, 26):
        user = User.objects.create_user(
            username=f"user{i}",
            email=f"user{i}@mail.com",
            password="h",
            role="jobseeker"
        )
        jobseeker.objects.create(
            user=user,
            jobseeker_name=f"Job Seeker {i}",
            experience=random.randint(1, 5),
            skills=["Python", "Django", "SQL"],
            resume="resume/sample.pdf"
        )
        users.append(user)

    # Create 25 Companies
    for i in range(1, 26):
        user = User.objects.create_user(
            username=f"company{i}",
            email=f"company{i}@mail.com",
            password="h",
            role="company"
        )
        company.objects.create(
            user=user,
            about_company=f"We are company {i}, building innovative solutions."
        )
        users.append(user)

    print("✅ 50 users created successfully!")

create_fake_users()