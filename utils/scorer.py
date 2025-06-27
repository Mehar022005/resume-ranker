import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Example skill keywords for simplicity
SKILL_KEYWORDS = ["python", "nlp", "machine learning", "aws", "sql", "pandas", "tensorflow", "communication"]

def clean_text(text):
    return re.sub(r"[^a-zA-Z ]", "", text.lower())

def extract_skills(text):
    return [skill for skill in SKILL_KEYWORDS if skill in text]

def rank_resumes(resumes, job_text, names):
    cleaned_job = clean_text(job_text)
    cleaned_resumes = [clean_text(r) for r in resumes]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([cleaned_job] + cleaned_resumes)
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    data = []
    skill_matrix = []
    for name, text, score in zip(names, cleaned_resumes, scores):
        skills = extract_skills(text)
        skill_row = [1 if skill in skills else 0 for skill in SKILL_KEYWORDS]
        skill_matrix.append(skill_row)
        missing = [s for s in SKILL_KEYWORDS if s not in skills]
        data.append({
            "Resume": name,
            "Score": round(score * 100, 2),
            "Matched Skills": ", ".join(skills),
            "Missing Skills": ", ".join(missing)
        })

    df = pd.DataFrame(data).sort_values(by="Score", ascending=False)
    return df, skill_matrix
