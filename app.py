# new

import streamlit as st
from gtts import gTTS
from io import BytesIO

# If you're using configuration, ensure it is placed in a dictionary
config = {
    "include_colab_link": True  # This is optional if you don't need this config.
}

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text)
    audio_buffer = BytesIO()
    tts.save(audio_buffer)
    audio_buffer.seek(0)  # Rewind the audio buffer to start
    return audio_buffer

# Streamlit app interface
st.title("Text to Speech")
st.write("Enter text and the app will convert it to speech")

text_input = st.text_input("Type something here")

if text_input:
    audio_output = text_to_speech(text_input)
    st.audio(audio_output, format="audio/mp3")
