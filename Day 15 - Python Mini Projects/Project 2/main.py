import streamlit as st 
from dotenv import load_dotenv
import io 
import os
import PyPDF2
import google.generativeai as genai

load_dotenv()
st.title("AI Resume Roaster")
st.divider()
st.badge("Mohit Khandale")
st.markdown("Upload Your Resume and get AI powered Roasting")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload your Resume here (PDF and txt only)", type=["pdf","txt"])
job_role = st.text_input("Enter the job role that you are targeting")
analyze = st.button("Analyze Resume")

def extract_text_from_pdf(file_bytes):
    reader =  PyPDF2.PdfReader(file_bytes)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def extract_data(uploaded_file):
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        with io.BytesIO(uploaded_file.read()) as file_bytes:
            return extract_text_from_pdf(file_bytes)
    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    
    
if uploaded_file and analyze:
    try:
        file_content = extract_data(uploaded_file)
        
        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()
        prompt = f""" you are a brutally honest, no non-sense HR excert who's been reviewing resumes for decades
        roast this resume like you are on a comedy stage but still give some useful insights feedback.
        Don't hold back - be sarcastic, witty and critical where needed.
        would make this resume actually land a job in {job_role} for a goode company.
        here is the resume, go wild:
        {file_content}
    
        make it sting and make sure to keep it in 150 words. Answer everything in hinglish
        """    
        #AI Callingu
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.markdown("## Analysis Result")
        st.markdown(response.text)
    
    except Exception as e:
        st.error(f"An Error Occured : {e}")