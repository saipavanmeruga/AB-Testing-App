
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


# load peft model from hub for inference
# config = PeftConfig.from_pretrained(model_id, config="https://huggingface.co/SaiPavanKumarMeruga/distilbert-base-uncased-lora-text-classification/blob/main/adapter_config.json")
inference_model = AutoModelForSequenceClassification.from_pretrained(
    'distilbert-base-uncased', num_labels=2, id2label=id2label, label2id=label2id
)
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
model = PeftModel.from_pretrained(inference_model, model_id)


placeholder_text = "Wow, what a great movie - complete waste of time."
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