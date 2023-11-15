# Import necessary modules from Flask
from flask import Flask, render_template, send_from_directory
import os
import random

# Create a Flask web application
app = Flask(__name__)

# Define the directory where audio files are stored
songs_directory = 'static/audio'

# Function to get a shuffled list of songs from the specified directory
def get_shuffled_song_list(directory):
    songs = []
    # Walk through the directory and its subdirectories to find audio files
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has a '.mp3' extension
            if file.endswith('.mp3'):
                # Add the file to the list of songs
                songs.append(file)
    # Shuffle the list of songs
    random.shuffle(songs)
    return songs

# Get the initial shuffled list of songs
songs = get_shuffled_song_list(songs_directory)

# Keep track of the current song index
current_song_index = 0  

# Define the route for the home page
@app.route('/')
def index():
    # Render the HTML template with the current song information and the list of songs
    return render_template('index.html', current_song=songs[current_song_index], songs=songs)

# Define a route for serving audio files
@app.route('/audio/<path:filename>')
def serve_audio(filename):
    # Send the requested audio file from the specified directory
    return send_from_directory(songs_directory, filename)

# Define a route for playing the next song
@app.route('/next')
def play_next():
    # Update the current song index to the next song in the list (circular, loops back to the beginning if at the end)
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    # Render the HTML template with the updated current song information and the list of songs
    return render_template('index.html', current_song=songs[current_song_index], songs=songs)

# Define a route for shuffling the list of songs
@app.route('/shuffle')
def shuffle_songs():
    # Shuffle the list of songs
    global current_song_index
    random.shuffle(songs)
    # Reset the current song index to the first song in the shuffled list
    current_song_index = 0
    # Render the HTML template with the current song information and the shuffled list of songs
    return render_template('index.html', current_song=songs[current_song_index], songs=songs)

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=False)

