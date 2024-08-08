from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy

# Load environment variables from .env file
load_dotenv()

# Get Spotify credentials from environment variables
SPOTIFY_ID = os.environ["SPOTIFY_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_SECRET"]
SPOTIPY_REDIRECT_URI = "http://localhost:3000"

# Authenticate with Spotify using OAuth
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Set the date for the Billboard Hot 100 chart
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Scrape the Billboard Hot 100 chart
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Initialize a list to store found songs
songs_found = []
count = 1

# Search for each song on Spotify
for song in song_names:
    query = song
    results = sp.search(q=query, type='track', limit=1)
    
    # Check if any tracks were found
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_info = {
            "track_name": track['name'],
            "track_uri": track['uri']
        }
        songs_found.append(track_info)
        count += 1

        # Print track details
        print(f"Track Name: {track['name']}")
        print(f"Track URI: {track['uri']}")
        print("-----------------------------")
        print(f"Count: {count}")
        print()

# Get current user's ID
user_id = sp.current_user()['id']

# Create a new private playlist
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist['id']

# Add found songs to the new playlist
track_uris = [track['track_uri'] for track in songs_found]
sp.playlist_add_items(playlist_id, track_uris)

print(f"Created playlist '{playlist_name}' with {len(track_uris)} songs.")
