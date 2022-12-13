import streamlit as st
import requests
import base64
import json

uploaded_file = st.file_uploader("Choose a file")


# Import the base64 encoding library.


# Pass the audio data to an encoding function.
def encode_audio(video):
    video_content = video.read()
    return base64.b64encode(video_content)
if uploaded_file is not None:
    # To read file as bytes:
    data = encode_audio(uploaded_file)
    video_bytes = uploaded_file.getvalue()
    st.video(video_bytes, format="video/mp4")
    button = st.button("Generate")
    if button:
        with st.spinner():
            response = requests.post("https://kabita-choudhary-get-text-from-video.hf.space/api/view_api", json={
                "data": [
                    {"name": uploaded_file.name,
                     "data": "data:video/mp4;base64," + str(data, 'ascii', 'ignore')},
                ]}).json()
            out = response["data"]
            output = out[0]
            st.text_area("Result", value=output, height=100)
