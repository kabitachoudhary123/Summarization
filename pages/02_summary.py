import streamlit as st
import requests
import base64

st.title("Generate Summary 🤗")

inp_text = st.text_area("Enter your text here.....", height=100)

button = st.button("Summary")

if button:
    with st.spinner():
        response_json = requests.post("https://kabita-choudhary-summary.hf.space/run/predict", json={
            "data": [
                inp_text,
            ]}).json()

        md = f"""
            <textarea rows="4" cols="50">
            {response_json['data'][0]}
            </textarea>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )