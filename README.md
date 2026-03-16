 AI Resume Screening System

An AI-powered Resume Screening System that automatically ranks resumes based on their similarity to a job description using Natural Language Processing techniques.

## Features

- Upload multiple resume PDFs
- Extract text from resumes automatically
- Compare resumes with job description
- Rank candidates based on similarity score
- Interactive web interface using Streamlit

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- PDFMiner
- Natural Language Processing (NLP)

## Machine Learning Method

The system uses:

TF-IDF Vectorization  
Cosine Similarity  

to measure the relevance between resumes and the job description.

## Project Workflow

Job Description
      ↓
Resume Upload
      ↓
Text Extraction
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Resume Ranking

## Project Structure

AI-Resume-Screening-System
│
├── app.py
├── parser.py
├── requirements.txt
├── README.md
└── resumes

## Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/AI-Resume-Screening-System.git

Navigate to project folder

cd AI-Resume-Screening-System

Install dependencies

pip install -r requirements.txt

## Run the Application

streamlit run app.py

## Example Use Case

Enter a job description and upload resumes.  
The system will automatically rank the candidates based on how closely their resumes match the job requirements.

## Future Improvements

- Skill extraction using NLP
- BERT embeddings for semantic similarity
- Resume scoring dashboard
- Recruiter analytics panel

## Author

Charith,  
M.Tech – Data Science & Artificial Intelligence,
IIIT DARWAD.
