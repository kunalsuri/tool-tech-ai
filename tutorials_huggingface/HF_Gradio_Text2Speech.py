# HF_Gradio_Text2Speech.py
# Python app to run a REST API endpoint from the HuggingFace Space and deslpay the result locally.

import requests
import streamlit as st
import pybase64

st.title("HuggingFace: Text to Speech API")

in_text = st.text_input("Please enter your text")
button = st.button ("Enter")

if button:
    with st.spinner():
        response_json = requests.post("https://abidlabs-speak.hf.space/run/predict", json={
            "data": [
                in_text,
                ]}).json()

        response_audio = f"""
            <audio controls>
            <source src="{response_json['data'][0]}" type="audio/flac">
            </audio>
            """

        st.markdown(
            response_audio,
            unsafe_allow_html=True,
        )
