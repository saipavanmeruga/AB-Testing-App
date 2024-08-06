---
base_model: roberta-base
library_name: peft
license: mit
metrics:
- accuracy
tags:
- generated_from_trainer
model-index:
- name: roberta-base-lora-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-lora-text-classification

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8264
- Accuracy: {'accuracy': 0.862}

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy            |
|:-------------:|:-----:|:----:|:---------------:|:-------------------:|
| No log        | 1.0   | 250  | 0.4008          | {'accuracy': 0.82}  |
| 0.6294        | 2.0   | 500  | 0.6326          | {'accuracy': 0.84}  |
| 0.6294        | 3.0   | 750  | 0.6141          | {'accuracy': 0.87}  |
| 0.3802        | 4.0   | 1000 | 1.2677          | {'accuracy': 0.82}  |
| 0.3802        | 5.0   | 1250 | 0.8264          | {'accuracy': 0.862} |


### Framework versions

- PEFT 0.12.0
- Transformers 4.42.4
- Pytorch 2.3.1
- Datasets 2.20.0
- Tokenizers 0.19.1