# Lyrics EmoBERT: Playlist Generator

## Project Overview

- **Description**: The project product is a playlist generator. Given the emotion, year, genre and the number of songs, the product can generate a playlist recommendation for users, which revolves around the advanced domain of Natural Language Processing (NLP), specifically focusing on sentiment analysis. The core model is finetuned from current huggingface SOTA model: Bert-base-uncased-emotion, reaching higher accuracy on the specific dataset.
- **Weakness of the current models**: Traditional sentiment analysis models often struggle with the complexity and emotional depth of song lyrics. These models may fail to capture the subtleties of language and emotion expressed in lyrics, leading to inaccurate or superficial analysis. This limitation hampers the ability to deeply understand and interpret the emotional content of songs, which can be valuable for various applications such as music recommendation, cultural studies, and emotional AI.
- **Approach**: To address this, the project involves fine-tuning a current state-of-the-art model, presumably based on the EmoBERT architecture, to better suit the task of sentiment analysis on song lyrics. Fine-tuning involves adjusting a pre-trained model to specialize in a specific task (in this case, sentiment analysis of lyrics). 
- **Solution Summary**: The fine-tuned model is expected to demonstrate a heightened ability to analyze and interpret emotions in song lyrics accurately. This enhanced capability allows for a deeper understanding of the emotional landscape in musical content, potentially contributing to more emotionally intelligent AI applications, improved user experiences in music streaming services, and richer cultural and linguistic studies.

## Model/Dataset Card
- **Model Used**: EmoBERT.
- **Dataset**: Collection of song lyrics (included in the 'lyrics' folder).
- **Sources**: References to the original sources of the model and dataset.
- **Permissions**: Information on dataset licensing and model usage rights.
- **Code**: [Link to the GitHub repository](https://github.com/SoniaWang121/lyrics-emo-bert/tree/main).

## Files in the Repository
- `app.py`: Flask application for model demonstration.
- `classify.py`: Script for classifying lyrics.
- `finetuner.py`: Code used for fine-tuning the EmoBERT model.
- `lyrics`: Folder containing the dataset used for fine-tuning.

## How to Run the Code
- **Dependencies**: List of dependencies and installation instructions.
- **Running the Scripts**: Detailed instructions on how to run `app.py`, `classify.py`, and `finetuner.py`.

## Critical Analysis
- **Impact**: Discuss how this fine-tuned model could affect the understanding of emotions in lyrics.
- **Insights**: Share insights on the challenges and successes encountered during fine-tuning.
- **Future Directions**: Ideas for further improving or extending the project.

## Resource Links
- **Further Reading**: Links to EmoBERT papers, sentiment analysis research, and relevant resources.
