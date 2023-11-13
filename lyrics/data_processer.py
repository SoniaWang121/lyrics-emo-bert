import json
import os
import pandas as pd
import re


# The function definitions remain the same
def clean_lyrics_corrected(lyric):
    lyric = re.sub(r'\[.*?\]', ' ', lyric)
    lyric = lyric.replace('\\n', ' ')
    # lyric = re.sub(r'Embed\"\", \s*\'default\'\s*$', '', lyric)
    # remove Embed"", 'default'
    # r'Embed\"\", \'default\'$'
    lyric = re.sub(r'Embed\", \'default\'$', ' ', lyric)
    lyric = lyric.strip('\"') 
    return lyric


def split_filename(filename):
    parts = filename.rsplit('__', 1)
    if len(parts) == 2:
        artist_name, title = parts
        artist_name = artist_name.replace('_', ' ')
        title = title.replace('_', ' ')
        return artist_name, title
    else:
        return None, None


def remove_title_from_lyrics(row):
    remove_string = row['title'] + ' Lyrics'
    if row['lyrics'].startswith(remove_string):
        return row['lyrics'].replace(remove_string, '', 1).strip()
    return row['lyrics']


data_type = 'test'
file_path = f'data/{data_type}.jsonl'
csv_file_path = file_path.replace('.jsonl', '.csv')
with open(file_path) as f:
    data = json.loads(f)
    data.to_csv(csv_file_path, index=False)

df = pd.read_csv(csv_file_path)

mood_to_int = {
    "anger": 3,
    "joy": 1,
    "sadness": 0,
}

# Applying split_filename first to create 'artist_name' and 'title'
df['artist_name'], df['title'] = zip(*df['lyrics_filename'].apply(split_filename))
# Finally applying clean_lyrics_corrected
df['lyrics'] = df['lyrics'].apply(clean_lyrics_corrected)
# Then applying remove_title_from_lyrics
df['lyrics'] = df.apply(remove_title_from_lyrics, axis=1)
# df = df[df['lyrics'].apply(lambda x: len(x) <= 400)]

# Dropping the 'lyrics_filename' column
df = df.drop('lyrics_filename', axis=1)

# Save 3 cats
df['mood'] = df['mood'].replace({'happy': 'joy', 'sad': 'sadness'})
# Remove rows where mood is 'calm'
df = df[df['mood'] != 'calm']
df['mood_cats'] = df['mood'].map(mood_to_int)

# Saving the updated dataframe to a new CSV file
output_file_path = f'data/{data_type}_cleaned.csv'
df.to_csv(output_file_path, index=False)