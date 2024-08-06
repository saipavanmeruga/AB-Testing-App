---
base_model: distilbert-base-uncased
library_name: peft
license: apache-2.0
metrics:
- accuracy
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-lora-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6464
- Accuracy: {'accuracy': 0.84}

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy            |
|:-------------:|:-----:|:----:|:---------------:|:-------------------:|
| No log        | 1.0   | 250  | 0.5728          | {'accuracy': 0.824} |
| 0.4384        | 2.0   | 500  | 0.6861          | {'accuracy': 0.84}  |
| 0.4384        | 3.0   | 750  | 1.1608          | {'accuracy': 0.812} |
| 0.1949        | 4.0   | 1000 | 1.0198          | {'accuracy': 0.826} |
| 0.1949        | 5.0   | 1250 | 1.1314          | {'accuracy': 0.838} |
| 0.0612        | 6.0   | 1500 | 1.3810          | {'accuracy': 0.844} |
| 0.0612        | 7.0   | 1750 | 1.6426          | {'accuracy': 0.832} |
| 0.0164        | 8.0   | 2000 | 1.6141          | {'accuracy': 0.844} |
| 0.0164        | 9.0   | 2250 | 1.6768          | {'accuracy': 0.842} |
| 0.0075        | 10.0  | 2500 | 1.6464          | {'accuracy': 0.84}  |


### Framework versions

- PEFT 0.12.0
- Transformers 4.42.4
- Pytorch 2.3.1
- Datasets 2.20.0
- Tokenizers 0.19.1