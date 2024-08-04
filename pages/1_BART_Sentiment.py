import transformers
import torch
import streamlit as st
import numpy as np
import streamlit.components.v1 as components


st.write('# Model 1: BART :sunglasses:')
st.write('Please wait for model to load')
pipe = transformers.pipeline(model="facebook/bart-large-mnli")
placeholder_text = "Wow, what a great movie - complete waste of time."
text_input = st.text_input(
        "Enter some text for the model to classify as Positive, Negative, or Neutral 👇",
        placeholder=placeholder_text)

candidate_labels=["Negative Sentiment", "Positive Sentiment", "Neutral Sentiment"]

if text_input == "":
    text_input = placeholder_text


results = pipe(text_input,
    candidate_labels=candidate_labels,
)
st.write(f"Predicted ➡️ {candidate_labels[np.argmax(results['scores'])]}")

components.iframe(f"https://forms.gle/2JsGm37jwhaeud9NA", height=1000)