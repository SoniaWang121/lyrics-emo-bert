# Lyrics EmoBERT: DIY Your Emotion Playlist in One Step

## Overview

### Introduction
EmoBERT is a playlist generator. Given the emotion, year, genre and the number of songs, the product can generate a playlist recommendation for users, which revolves around the advanced domain of Natural Language Processing, specifically focusing on sentiment analysis. The core model is finetuned from current huggingface SOTA model: Bert-base-uncased-emotion, reaching higher accuracy on the specific dataset.

### Approach
* Finetune the current SOTA model, based on the BERT architecture.
* Specialize in the task sentiment analysis of lyrics task.


## 🌟 Model Finetuning
### Model Card
Explore the intricate details of our [model](https://huggingface.co/sonia12138/bert-base-uncased-emotion-fituned) in its full glory on HuggingFace! 🤖✨
![Marvel at our Model!](https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/model_card.png)

## 🚀 Downstream Task
### Task: Text Classification (Sentiment Analysis)
The challenge: Text Classification with a twist of Emotion Analysis! 🎭📝

Our quest begins in the realm of sentiment, where words convey more than just meaning. However, the path isn't straightforward. The absence of a well-labeled, comprehensive dataset for song lyrics in this domain led us to merge multiple datasets, creating a unique blend suited for our purpose.

### Multi-faceted Music Dataset
Dive into our [dataset's](https://huggingface.co/datasets/sonia12138/lyrics-emotion) universe here! 🌌📊

<img src="https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/dataset-1.png" width="50%" height="50%">
<img src="https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/dataset-2.png" width="50%" height="50%">
<img src="https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/dataset.png" width="50%" height="80%">

## 💡 Interactive Demonstration
Step into our [interactive domain](https://huggingface.co/spaces/sonia12138/playlist-generator) where AI meets creativity! 🎨🤖
![Interactive Wonderland](https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/demostration.png)

## 💻 Code Demonstration
Unleash the power of our model in your own experiments on [Google Colab](https://colab.research.google.com/drive/1y2i56MLstUYJ5W02pwD0UJlDHjQCuC3r?usp=sharing)! 💻🔥
![Code Adventure](https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/colab.png)

## 📖 Learning from Challenges
* The absence of a golden standard for lyrics emotion. 
* This experience underlined the importance of dataset standardization could lead to more universally applicable models with broader generalization capabilities.

<img src="https://github.com/SoniaWang121/lyrics-emo-bert/blob/main/images/low-accuracy.png" width="80%" height="80%">

## Critical Analysis
### Impact:
* Enhanced Emotion Recognition in Lyrics
* Personalized Music Experience
  
### Insights
* Challenges in Fine-Tuning
* Scaricity of current relevant datasets
### Future Directions
* Expanding Emotional Range
* Integrating with Music Features
* Broader Applications

## Video Recording
[Video of the overview](https://youtu.be/6UgXjMW7Dcs)
## More Resources
* [Baseline model](https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion)
* [Finetune a pretrained model](https://huggingface.co/docs/transformers/training)
* [Huggingface notebook](https://huggingface.co/docs/transformers/notebooks)
* [Gradio Github](https://github.com/gradio-app/gradio)

