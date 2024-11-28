import streamlit as st
import pyttsx3
from io import BytesIO

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to convert text to speech using pyttsx3
def text_to_speech(text):
    # Save the speech to a temporary audio file
    audio_file = BytesIO()
    engine.save_to_file(text, audio_file)
    audio_file.seek(0)  # Move the cursor to the beginning of the file
    return audio_file

# Streamlit app interface
st.title("Text to Speech")
st.write("Enter text and the app will convert it to speech.")

# User input for text
text_input = st.text_input("Type something here:")

if text_input:
    audio_output = text_to_speech(text_input)
    st.audio(audio_output, format="audio/wav")
