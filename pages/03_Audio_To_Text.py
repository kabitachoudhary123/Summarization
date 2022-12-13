import streamlit as st
import requests
import base64
import json

uploaded_file = st.file_uploader("Choose a file")


# Import the base64 encoding library.


# Pass the audio data to an encoding function.
def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content)
if uploaded_file is not None:
    # To read file as bytes:
    data = encode_audio(uploaded_file)
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format='audio/mp3')


    # bytes_data = uploaded_file.getvalue()
    # st.write(data)
    button = st.button("Translate")

    if button:
        with st.spinner():
            response = requests.post("https://kabita-choudhary-audio-to-text.hf.space/api/predict", json={
                "data": [
                    {"name": uploaded_file.name,
                     "data": "data:audio/mp3;base64," + str(data, 'ascii', 'ignore')},
                ]}).json()
            out = response["data"]
            output = out[0]
            st.text_area("Result", value=output, height=100)
