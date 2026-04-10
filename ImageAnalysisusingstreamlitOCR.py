import google.generativeai as genai
import streamlit as st
from PIL import Image
genai.configure(api_key="AIzaSyC8XK2ngJhptPwZPKtdOy1xjuBt2nnwJ8M")
model=genai.GenerativeModel("gemini-2.5-flash")  
st.title("Image Q/A with Gemini")
x = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "AVIF"])
prompt =st.text_input("Enter your question about the image:")
myprompt = "You are a Document Analysis and OCR & Table Extraction Expert. Analyze document scan images to perform OCR, extract tables, and convert them to structured CSV format.Extract all text from the image using OCR, identify any tables, preserve their structure, and convert them into a clean, well-formatted CSV output."
if st.button('submit'):
    img=Image.open(x)
    response  = model.generate_content([img, prompt ,myprompt])
    st.write(response.text)