# 🤖 AI Resume Ranker

An intelligent Streamlit-based web app that ranks uploaded resumes based on their relevance to a given job description using NLP and machine learning techniques.

---

## 🚀 Features

- 📝 Enter Job Description in a text area
- 📄 Upload multiple resumes (PDF)
- 🧠 Ranks resumes using smart text similarity (TF-IDF + Skill Matching)
- 📊 Visuals: Resume Score Bar Chart and Skill Match Heatmap
- 📥 Download results as CSV
- 🔍 Shows matched and missing key skills

---

## 📦 Installation

1. **Clone the repository or unzip**
2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app/main.py
```

Then open the link (usually `http://localhost:8501`) in your browser.

---

## 📁 Project Structure

```
AI_Resume_Ranker/
│
├── app/
│   └── main.py               # Streamlit frontend
│
├── utils/
│   ├── parser.py             # PDF/text parsing
│   ├── scorer.py             # Resume ranking logic
│   └── visuals.py            # Charts & heatmaps
│
├── data/
│   ├── resumes/              # Sample resumes (PDF)
│   └── job_desc/             # Sample job descriptions
│
├── output/                   # Optional output folder
├── requirements.txt
└── README.md
```

---

## 💡 Future Ideas

- Resume feedback and suggestions
- Smart skill extraction via Named Entity Recognition (NER)
- AI-powered JD generator
- Login system with user history

---

## 🛠 Built With

- [Streamlit](https://streamlit.io)
- [scikit-learn](https://scikit-learn.org/)
- [PyMuPDF](https://pymupdf.readthedocs.io)
- [pandas, seaborn, matplotlib]

---

## 🧑‍💻 Author

Made by [Your Name] — for educational and career-boosting purposes!

---
