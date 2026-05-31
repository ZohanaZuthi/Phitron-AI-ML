import io
from gtts import gTTS
import streamlit as st

from PIL import Image
from google import genai
from dotenv import load_dotenv

import os

# loading the environment
load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")


# initializing a client
client=genai.Client(api_key=api_key)


# note generator:
def note_generator(img):
    image=[Image.open(image) for image in img]
    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=image+["Summarize the picture in note format at max 100 make sure to add necessary markdown to differentiate different section"]
)
       
    return response.text
def audio_transcription(text):
    speech=gTTS(text, lang='en', slow=False)

    audio_buffer=io.BytesIO()

    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_maker(img,difficulty):
    image=[Image.open(image) for image in img]
    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=image+["Generate 5 quiz questions with answers based on the picture. Make sure to include the difficulty level which is "+difficulty]
)
       
    return response.text
    