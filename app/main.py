from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Mock job postings data
job_postings = [
    {"job_id": 1, "job_title": "Software Engineer", "company": "Tech Solutions Inc.", "required_skills": ["JavaScript", "React", "Node.js"], "location": "San Francisco", "job_type": "Full-Time", "experience_level": "Intermediate"},
    {"job_id": 2, "job_title": "Data Scientist", "company": "Data Analytics Corp.", "required_skills": ["Python", "Data Analysis", "Machine Learning"], "location": "Remote", "job_type": "Full-Time", "experience_level": "Intermediate"},
    # More job postings here...
]

# User profile model
class Preferences(BaseModel):
    desired_roles: List[str]
    locations: List[str]
    job_type: str

class UserProfile(BaseModel):
    name: str
    skills: List[str]
    experience_level: str
    preferences: Preferences

# Helper function for skill match
def skill_match(user_skills, job_skills):
    return len(set(user_skills) & set(job_skills)) / len(set(job_skills))

@app.post("/recommend")
def recommend_jobs(user_profile: UserProfile):
    recommendations = []
    for job in job_postings:
        # Match jobs based on skills, experience level, location, and job type
        skill_score = skill_match(user_profile.skills, job["required_skills"])
        experience_match = user_profile.experience_level == job["experience_level"]
        location_match = job["location"] in user_profile.preferences.locations or "Remote" in user_profile.preferences.locations
        job_type_match = user_profile.preferences.job_type == job["job_type"]

        if skill_score > 0 and experience_match and location_match and job_type_match:
            recommendations.append(job)

    if not recommendations:
        raise HTTPException(status_code=404, detail="No matching jobs found")
    
    return recommendations
