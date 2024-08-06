
import streamlit as st
import numpy as np
import streamlit.components.v1 as components
import torch
from peft import PeftConfig, PeftModel
from transformers import AutoTokenizer,AutoModelForSequenceClassification


#define label maps
id2label = {0:'NotSarcastic', 1: 'Sarcastic'}
label2id = {'NotSarcastic':0, 'Sarcastic':1}

st.write('# Model A: :sunglasses:')
st.write('Please wait for model to load')

model_checkpoint = "distilbert-base-uncased"
model_id = "SaiPavanKumarMeruga/"+model_checkpoint+"-lora-sarcasm-classification"

# how to load peft model from hub for inference
config = PeftConfig.from_json_file('./pages/distilbert-base-uncased-lora-text-classification/adapter_config.json')
inference_model = AutoModelForSequenceClassification.from_pretrained(
    './pages/distilbert-base-uncased-lora-text-classification/', num_labels=2, id2label=id2label, label2id=label2id
)
tokenizer = AutoTokenizer.from_pretrained('./pages/distilbert-base-uncased-lora-text-classification/')
model = PeftModel.from_pretrained(inference_model, './pages/distilbert-base-uncased-lora-text-classification/')


placeholder_text = "Flustered mathematician unable to recommend good number"
text_input = st.text_input(
        "Enter some text for the model to classify as Sarcastic, Not Sarcastic 👇",
        placeholder=placeholder_text)


if text_input == "":
    text_input = placeholder_text


try:
    inputs = tokenizer.encode(text_input, return_tensors="pt")
    logits = model(inputs).logits
    predictions = torch.max(logits,1).indices

    st.write(f"Predicted ➡️ {id2label[predictions.tolist()[0]]}")

except Exception as e:
    st.write("Error occured while processing the sentence")

components.iframe(f"https://forms.gle/DQZjdYc9qGFxsFcE7", height=1000)