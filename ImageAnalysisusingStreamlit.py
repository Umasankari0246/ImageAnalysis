import google.generativeai as genai
import streamlit as st
from PIL import Image
genai.configure("API KEY")
model=genai.GenerativeModel('gemini-2.5-flash')
st.title ("Image Q&A with Gemini")
a=st.file_uploader("Upload an image", type = ["jpg","jpeg","png"])
prompt=st.text_input("enter the question")

if st.button('submit'):
    img= Image.open(a)
    response = model.generate_content([img,prompt])
    st.write(response.text)
