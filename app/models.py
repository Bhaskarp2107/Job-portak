from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobPosting(Base):
    __tablename__ = 'job_postings'
    job_id = Column(Integer, primary_key=True)
    job_title = Column(String)
    company = Column(String)
    required_skills = Column(String)
    location = Column(String)
    job_type = Column(String)
    experience_level = Column(String)
