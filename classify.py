import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification, TextClassificationPipeline
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report

tokenizer = BertTokenizer.from_pretrained('bhadresh-savani/bert-base-uncased-emotion')
# ---------- finetuning model ---------- 
model_path = 'dair-ai-emotion/results'
model_file = 'pytorch_model.bin'
model = BertForSequenceClassification.from_pretrained(model_path, 
                                                      config=model_path + '/config.json')
model.load_state_dict(torch.load(model_path + '/' + model_file))

# # ---------- baseline v1 ---------- 
# model = BertForSequenceClassification.from_pretrained('bhadresh-savani/bert-base-uncased-emotion')

# Create a pipeline for text classification
classifier = TextClassificationPipeline(model=model, tokenizer=tokenizer, truncation=True, max_length=512, return_all_scores=True)

# Read the cleaned CSV file
# df = pd.read_csv('dair-ai-emotion/data/test.csv')
# df = pd.read_csv('lyrics/data/test_cleaned.csv')
df = pd.read_csv('Original_Songs_Lyrics_with_French_Translation/data/train.csv')
df = df[df['language'] == 'en']

mod_to_int = {
    "anger": 3,
    "fear": 4,
    "joy": 1,
    "love": 2,
    "sadness": 0,
    "surprise": 5
}

# Initialize columns for predicted mood and score
df['mood_pred'] = None
df['score'] = None

true_labels = []
predicted_labels = []

# Process each row in the DataFrame
for index, row in df.iterrows():
    # Classify the sentiment of the lyrics
    prediction = classifier(row['original_version'])
    # Select the emotion with the highest score
    top_prediction = max(prediction[0], key=lambda x: x['score'])
    # Assign the predicted emotion and its score to the DataFrame
    df.at[index, 'mood_pred'] = top_prediction['label']
    df.at[index, 'score'] = top_prediction['score']

    # true_labels.append(row['label'])
    # predicted_labels.append(top_prediction['label'])

    # Print progress every 100 lines to monitor the process
    if (index + 1) % 100 == 0:
        print(f'Processed {index + 1} lines')

# predicted_labels = df['mood_pred'].map(mod_to_int).tolist()

# # Calculate metrics
# accuracy = accuracy_score(true_labels, predicted_labels)
# recall = recall_score(true_labels, predicted_labels, average='macro')
# f1 = f1_score(true_labels, predicted_labels, average='macro')

# print(f'Accuracy: {accuracy}')
# print(f'Recall: {recall}')
# print(f'F1 Score: {f1}')
# # Optional: print detailed classification report
# print(classification_report(true_labels, predicted_labels))   

# df.to_csv('lyrics/data/classified_test.csv')
df.to_csv('Original_Songs_Lyrics_with_French_Translation/data/classified_train.csv')

      