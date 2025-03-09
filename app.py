import streamlit as st
import pdfplumber
import docx2txt
import spacy
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure SpaCy model is available
model_name = "en_core_web_sm"
try:
    nlp = spacy.load(model_name)
except OSError:
    os.system(f"python -m spacy download {model_name}")
    nlp = spacy.load(model_name)

st.title("📄 AI-Powered Resume Screening & Ranking System")

# Job Description Input
job_description = st.text_area("📝 Enter Job Description:")

uploaded_files = st.file_uploader("📂 Upload Resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files and job_description:
    resume_texts = []
    resume_names = []

    # Extract text from resumes
    for uploaded_file in uploaded_files:
        text = ""
        if uploaded_file.name.endswith(".pdf"):
            with pdfplumber.open(uploaded_file) as pdf:
                text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        elif uploaded_file.name.endswith(".docx"):
            text = docx2txt.process(uploaded_file)
        
        resume_texts.append(text)
        resume_names.append(uploaded_file.name)
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    all_texts = [job_description] + resume_texts
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compute Similarity Scores
    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]
    similarity_scores = cosine_similarity(job_vec, resume_vecs).flatten()
    
    # Rank Resumes
    ranked_resumes = sorted(zip(resume_names, similarity_scores), key=lambda x: x[1], reverse=True)
    
    # Display Results
    st.subheader("📊 Ranked Resumes")
    for i, (name, score) in enumerate(ranked_resumes, start=1):
        st.write(f"{i}. **{name}** - Similarity Score: {score:.2f}")
