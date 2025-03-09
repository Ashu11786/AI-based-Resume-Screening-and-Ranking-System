# AI-Powered Resume Screening and Ranking System

## Overview
This project is an AI-driven resume screening system that ranks resumes based on their relevance to a job description. It leverages **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques to extract key skills and qualifications from resumes and compare them with job requirements.

## Features
- Upload resumes in **PDF/DOCX** format.
- Extract text using **pdfplumber** and **docx2txt**.
- Preprocess text using **SpaCy** and **NLTK**.
- Rank resumes using **TF-IDF Vectorization** and **Cosine Similarity**.
- User-friendly **Streamlit-based** interface for recruiters.

## Technology Stack
- **Backend**: Python
- **Frontend**: Streamlit
- **Libraries**:
  - `spaCy`, `NLTK` - NLP processing
  - `Scikit-learn` - ML-based ranking
  - `pdfplumber`, `docx2txt` - Resume text extraction

## Installation
Clone the repository and install the required dependencies:
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
```
Download the **SpaCy language model**:
```sh
python -m spacy download en_core_web_sm
```

## Running the Application
Start the Streamlit application:
```sh
streamlit run app.py
```

## 🔗 Live Demo
Access the app here: [AI-Powered Resume Screening App](https://mukd2jme7eb98s7ckj36aq.streamlit.app/)

## 📸 Screenshot
![App Screenshot](screenshot.png)

## How to Access the Deployed App
If the app is deployed on **Streamlit Cloud**, share the app link with users.
```
https://mukd2jme7eb98s7ckj36aq.streamlit.app/
```
Anyone with the link can access the app in their browser.

## Deployment on Streamlit Cloud
To deploy your app:
1. Push your code to a **public GitHub repository**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in.
3. Click **New App** and connect your GitHub repo.
4. Select `app.py` as the main script.
5. Click **Deploy**.

## License
This project is open-source and available under the **MIT License**.

## Contact
For queries, open an issue or reach out via GitHub discussions.

