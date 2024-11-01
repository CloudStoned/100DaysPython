import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Spotify credentials from environment variables
SPOTIFY_ID = os.environ["SPOTIFY_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_SECRET"]

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Search for a song
query = "Shape of You"  # Replace with the song title
results = spotify.search(q=query, type='track', limit=1)
track = results['tracks']['items'][0]
print(f"Track Name: {track['name']}")
print(f"Track URI: {track['uri']}")
