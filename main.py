from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ResumeInput(BaseModel):
    resume_text: str

SKILLS_DB = {
    "AI/ML": ["python", "machine learning", "deep learning", "nlp", "tensorflow", "pytorch"],
    "Web Development": ["html", "css", "javascript", "react", "node"],
    "Data Science": ["pandas", "numpy", "matplotlib", "seaborn", "sql"]
}
@app.post("/analyze")
def analyze_resume(input: ResumeInput):
    text = input.resume_text.lower()

    domain_scores = {}
    detected_skills = []

    for domain, skills in SKILLS_DB.items():
        domain_scores[domain] = 0
        for skill in skills:
            if skill in text:
                detected_skills.append(skill)
                domain_scores[domain] += 10

    # Find best matching domain
    detected_domain = max(domain_scores, key=domain_scores.get)
    score = domain_scores[detected_domain]

    suggestions = []

    if score < 30:
        suggestions.append("Consider adding more relevant technical skills.")

    # Suggest missing skills
    missing_skills = []

    for skill in SKILLS_DB[detected_domain]:
        if skill not in detected_skills:
            missing_skills.append(skill)

    if missing_skills:
        suggestions.append(f"Consider learning: {', '.join(missing_skills[:3])}")

    return {
        "detected_skills": list(set(detected_skills)),
        "domain": detected_domain,
        "resume_score": score,
        "suggestions": suggestions
    }
