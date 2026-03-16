import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from parser import extract_resume_text

st.title("AI Resume Screening System")

job_description = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader("Upload Resumes", type="pdf", accept_multiple_files=True)

if st.button("Analyze Resumes"):

    resumes = []
    names = []

    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

        text = extract_resume_text(file.name)
        resumes.append(text)
        names.append(file.name)

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    job_vector = vectors[0]

    scores = []

    #vectors.shape is a tuple (n_samples, n_features); use the first element (n_samples)
    for i in range(1, vectors.shape[0]):
        similarity = cosine_similarity(job_vector, vectors[i])[0][0]
        scores.append((names[i-1], similarity))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    st.subheader("Resume Ranking")

    for name, score in scores:
        st.write(f"{name} : {round(score*100,2)}% match")

        