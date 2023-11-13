import gradio as gr
import pandas as pd

data_dir = 'Original_Songs_Lyrics_with_French_Translation/data/classified_train.csv'
df = pd.read_csv(data_dir)

def generate_song(emotion, genre, number_of_songs, year):
    # Filter the DataFrame based on the user input
    # filtered_df = df[(df['mood_pred'] == emotion.lower()) & (df['genre'] == genre) & (df['year'] == year)]
    filtered_df = df[(df['mood_pred'] == emotion.lower()) & (df['year'] >= year)]

    # Limit the number of results
    limited_df = filtered_df.head(number_of_songs)

    # Prepare the output string with the titles of the songs
    song_info = [f"{row['title']} ----- {row['artist_name']}" for _, row in limited_df.iterrows()]
    output = f"Generated {len(song_info)} song(s) in the genre of {genre} with a {emotion} emotion from year {year}:\n" \
            + "\n\n".join(song_info)    

    return output

# Create dropdown options for emotion and genre - replace with actual options
emotion_options = ['Joy', 'Sadness', 'Fear', 'Surprise', 'Anger', 'Love']
genre_options = ['Rock', 'Pop', 'Jazz', 'Classical']


iface = gr.Interface(
    fn=generate_song,
    inputs=[
        gr.Dropdown(choices=emotion_options, label="Emotion"),
        gr.Dropdown(choices=genre_options, label="Genre"),
        gr.Slider(minimum=1, maximum=15, step=1, label="Number of Songs"),
        gr.Slider(minimum=1950, maximum=2023, step=1, label="Year")
    ],
    outputs="text",
    title="Playlist Generator",
    description="Select emotion and genre, then adjust the number of songs and year to generate a song."
)


iface.launch(debug=True)