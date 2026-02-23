from app.models import job, company
import random
from django.db import transaction

def create_fake_jobs():

    job_titles = [
        "Backend Developer",
        "Frontend Developer",
        "Fullstack Developer",
        "DevOps Engineer",
        "Data Analyst",
        "Mobile App Developer",
        "UI/UX Designer",
        "QA Engineer",
        "Cybersecurity Analyst",
        "Machine Learning Engineer"
    ]

    employment_types = ["Full-time", "Part-time", "Contract", "Remote"]

    skills_pool = [
        "Python", "Django", "React", "SQL",
        "Docker", "AWS", "Flutter",
        "TensorFlow", "Figma", "Linux"
    ]

    responsibilities_sample = [
        "Develop scalable applications",
        "Collaborate with cross-functional teams",
        "Write clean and maintainable code",
        "Optimize performance",
        "Participate in code reviews"
    ]

    requirements_sample = [
        "Strong problem-solving skills",
        "Good communication",
        "Experience with modern frameworks",
        "Understanding of REST APIs",
        "Ability to work in a team"
    ]

    companies = company.objects.all()
    job_count = 0

    with transaction.atomic():
        for comp in companies:
            for _ in range(2):
                job.objects.create(
                    company=comp,
                    job_title=random.choice(job_titles),
                    responsibility=random.sample(responsibilities_sample, 3),
                    requirement=random.sample(requirements_sample, 3),
                    employment_type=random.choice(employment_types),
                    min_salary=random.randint(500, 1500),
                    max_salary=random.randint(2000, 5000),
                    experience_required=random.randint(1, 5),
                    skills_required=random.sample(skills_pool, 4),
                )
                job_count += 1

    print(f"✅ {job_count} jobs created successfully!")


create_fake_jobs()