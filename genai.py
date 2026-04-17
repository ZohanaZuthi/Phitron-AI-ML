from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.environ.get('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)
print(api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain Gemini API in 100 words"
)

st.markdown("### Response from Gemini API")
st.write(response.text)
