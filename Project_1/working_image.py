import streamlit as st
from api_calling import note_generator

from PIL import Image
from google import genai
from dotenv import load_dotenv

import os

# loading the environment
load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")


# initializing a client
client=genai.Client(api_key=api_key)


# /title
st.title("Note summary and quiz generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    
    # image
    images=st.file_uploader(
        "Upload the photos",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )
    
    if images:
        contents=[]
        
        for img in images:
            image=Image.open(img)
            contents.append(image)
        response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[contents,"Summarize the picture in note format at max 100 make sure to add necessary markdown to differentiate different section"]
    )
        st.markdown(response.text)