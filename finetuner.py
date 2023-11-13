import json
from sklearn.model_selection import train_test_split
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import Trainer, TrainingArguments
from torch.utils.data import Dataset
import pandas as pd


# 创建数据集
class Dataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
        assert len(encodings['input_ids']) == len(labels)


    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        # item = {key: val[idx] for key, val in self.encodings.items()} # No need for torch.tensor here
        item['labels'] = torch.tensor(self.labels[idx])
        return item


    def __len__(self):
        return len(self.labels)


# 读取数据
train_data = pd.read_csv('dair-ai-emotion/data/train.csv')
val_data = pd.read_csv('dair-ai-emotion/data/test.csv')
# data = pd.read_csv('data/test.csv')
# train_data, val_data = train_test_split(data, test_size=0.2)

# 加载预训练模型和分词器
model_name = "bhadresh-savani/bert-base-uncased-emotion"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=6)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# tokenized_data = tokenize_function(train_data)
# tokenized_data = tokenize_function(train_data['lyrics'].tolist())

train_encodings = tokenizer(train_data['text'].tolist(), padding='max_length', truncation=True, return_tensors='pt')
val_encodings = tokenizer(val_data['text'].tolist(), padding='max_length', truncation=True, return_tensors='pt')

train_dataset = Dataset(train_encodings, train_data['label'])
val_dataset = Dataset(val_encodings, val_data['label'])

# 训练参数
training_args = TrainingArguments(
    output_dir='./results',          
    num_train_epochs=8,              
    per_device_train_batch_size=32,  
    per_device_eval_batch_size=64,   
    warmup_steps=500,                
    weight_decay=0.01,               
    logging_dir='./logs',            
)

# 初始化Trainer
trainer = Trainer(
    model=model,                         
    args=training_args,                  
    train_dataset=train_dataset,         
    eval_dataset=val_dataset             
)

# Fine-tuning
trainer.train()

model_save_path = 'results'
trainer.save_model(model_save_path)

# 评估模型
evaluation_results = trainer.evaluate()
evaluation_dict = dict(evaluation_results)

# 保存评估结果为JSON
with open('evaluation_results.json', 'w') as f:
    json.dump(evaluation_dict, f, indent=4)

# 混淆矩阵
from sklearn.metrics import confusion_matrix
predictions = trainer.predict(val_dataset)
conf_matrix = confusion_matrix(predictions.label_ids, predictions.predictions.argmax(-1))

# 计算准确率、召回率、F1分数
from sklearn.metrics import accuracy_score, recall_score, f1_score
accuracy = accuracy_score(predictions.label_ids, predictions.predictions.argmax(-1))
recall = recall_score(predictions.label_ids, predictions.predictions.argmax(-1), average='macro')
f1 = f1_score(predictions.label_ids, predictions.predictions.argmax(-1), average='macro')
print(f'accuracy: {accuracy}')
print(f'recall: {recall}')
print(f'f1: {f1}')