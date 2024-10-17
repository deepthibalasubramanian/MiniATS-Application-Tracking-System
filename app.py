import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv

# load all the environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Response
def get_gemini_response(input_prompt):
    #load the model
    model = genai.GenerativeModel('gemini-pro')
    #generate the response
    response = model.generate_content(input_prompt)
    return response.text

# convert pdf to text
def input_pdf_to_text(uploaded_pdf_file):
    # Read the file via instance of pdfreader
    reader = pdf.PdfReader(uploaded_pdf_file)
    text=""
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        text += str(page.extract_text())
    return text

# Creating prompt template
input_prompt='''
Act like a skilled and experienced Application Tracking System (ATS) 
with a very deep understanding of technology and its related fields, 
including but not restricted to Software Engineering, Data Science, 
Data Analysis, Artificial Intelligence, Machine Learning, Cloud 
Computing, Cybersecurity, Networks, Operating Systems, Database 
Systems and Big Data Engineering. Your task is to evaluated the 
resume based on the provided job description and rate the profile 
of the candidate accurarely, with respect to how suitable their 
skillset is with respect to the job posting. You must consider the 
job market to be extremely competitive and also provide best assistance 
for improving the resumes. Assign percentage matching based on the 
Job Description and list the missing keywords with high accuracy
resume:{text}
description:{jd}
I want the response in one single string having the structure
{{"JD Match":" %";      "MissingKeywords: []";      "Profile Summary":""}}
'''

# streamlit app
st.title("ATS-scored Resume Evaluator")
st.text("Improve your Resume ATS Score")
jd = st.text_area("Paste the Job Description")
uploaded_pdf_file = st.file_uploader("Upload your Resume", type="pdf", help="Please upload as PDF")
submit = st.button("Submit")

if submit:
    if uploaded_pdf_file is not None:
        text = input_pdf_to_text(uploaded_pdf_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)