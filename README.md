# Lyrics EmoBERT: Playlist Generator

## Overview

### What is EmoBERT? 

EmoBERT is a playlist generator. Given the emotion, year, genre and the number of songs, the product can generate a playlist recommendation for users, which revolves around the advanced domain of Natural Language Processing (NLP), specifically focusing on sentiment analysis. The core model is finetuned from current huggingface SOTA model: Bert-base-uncased-emotion, reaching higher accuracy on the specific dataset.

### What Data Can We Use?

- **Approach**: To address this, the project involves fine-tuning a current state-of-the-art model, presumably based on the EmoBERT architecture, to better suit the task of sentiment analysis on song lyrics. Fine-tuning involves adjusting a pre-trained model to specialize in a specific task (in this case, sentiment analysis of lyrics). 
- **Solution Summary**: The fine-tuned model is expected to demonstrate a heightened ability to analyze and interpret emotions in song lyrics accurately. This enhanced capability allows for a deeper understanding of the emotional landscape in musical content, potentially contributing to more emotionally intelligent AI applications, improved user experiences in music streaming services, and richer cultural and linguistic studies.

## Interactive demostration

[Welcome to try out the demo here](https://github.com/SoniaWang121/lyrics-emo-bert/tree/main).

![image text](https://github.com/SoniaWang121/lyrics-emo-bert/blob/Kun-Peng/demostration.png)

## Model/Dataset Card
### Model Performance Comparision
| Model                          | Accuracy | Recall | F1 Score | 
| ------------------------------ | -------- | -------- | -------- | 
| Distilbert-base-uncased-emotion |      |     |                
| Bert-base-uncased-emotion      |   92.6  |   87.9  |        88.2        
| Roberta-base-emotion           |     |    |                
| Albert-base-v2-emotion         |     |    |                 
| **Ours**             |   92.9  |  88  |          88.5       
- **Model Used**: EmoBERT.
- **Dataset**: Collection of song lyrics (included in the 'lyrics' folder).
- **Sources**: References to the original sources of the model and dataset.
- **Permissions**: Information on dataset licensing and model usage rights.
- **Code**: [Link to the GitHub repository](https://github.com/SoniaWang121/lyrics-emo-bert/tree/main).
## Critical Analysis
- **Impact**: Discuss how this fine-tuned model could affect the understanding of emotions in lyrics.
- **Insights**: Share insights on the challenges and successes encountered during fine-tuning.
- **Future Directions**: Ideas for further improving or extending the project.

## Resource Links
- [](https://github.com/SoniaWang121/lyrics-emo-bert/tree/main).
