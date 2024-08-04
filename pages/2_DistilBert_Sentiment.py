import transformers
import torch
import streamlit as st
import numpy as np
import streamlit.components.v1 as components


st.write('# Model 2: DistilBert Fine-tuned ⚗️')
st.write('Please wait for model to load')

#Trained on the SST2 dataset
pipe = transformers.pipeline(model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
placeholder_text = "Wow, what a great movie - complete waste of time."
text_input = st.text_input(
        "Enter some text for the model to classify as Positive, Negative, or Neutral 👇",
        placeholder=placeholder_text)

if text_input == "":
    text_input = placeholder_text

st.write(f"Predicted ➡️ {pipe(text_input)[0]['label']}")

components.iframe(f"https://forms.gle/FMdCsq3Qse4MGgc2A", height=1000)