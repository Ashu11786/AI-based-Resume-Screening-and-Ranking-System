%%writefile app.py
import streamlit as st
import pdfplumber
import docx2txt
import spacy

st.title("📄 AI-Powered Resume Screening System")

uploaded_file = st.file_uploader("📂 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif uploaded_file.name.endswith(".docx"):
        text = docx2txt.process(uploaded_file)

    st.subheader("Extracted Resume Text:")
    st.text(text[:500])  # Show first 500 characters

    # NLP Processing
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ == "NOUN"]

    st.subheader("🛠 Extracted Skills:")
    st.write(skills)
