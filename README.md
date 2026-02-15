Resume Analyzer API
🚀 Project Overview

A RESTful API built using FastAPI that analyzes resume text, detects technical skills, identifies the candidate's domain, calculates a resume score, and provides improvement suggestions.

🛠 Tech Stack

Python

FastAPI

Uvicorn

📌 Features

Skill detection

Domain classification

Resume scoring logic

Skill improvement suggestions

🔍 API Endpoint
POST /analyze

Example Input:

{
  "resume_text": "I know Python, Machine Learning and SQL"
}


Example Output:

{
  "detected_skills": ["python", "machine learning"],
  "domain": "AI/ML",
  "resume_score": 30,
  "suggestions": []
}

▶️ How to Run

Create virtual environment

Install dependencies:

pip install -r requirements.txt


Run server:

uvicorn main:app --reload


Open:

http://127.0.0.1:8000/docs
