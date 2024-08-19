import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set up environment variables for Spotify API credentials and redirect URI
os.environ['SPOTIPY_CLIENT_ID'] = 'ca72b4bdf1e44042ba7a2aeabeff51a7'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'd40920bd9409491ba248e525889b1c8a'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:3000/callback'

# Authenticate with Spotify using OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-read-private playlist-modify-public playlist-modify-private"))

def list_user_playlists():
    playlists = sp.current_user_playlists()  # Fetch the user's playlists
    playlist_dict = {}  # Initialize an empty dictionary to store playlist names and IDs
    for playlist in playlists['items']:  # Iterate through each playlist
        playlist_dict[playlist['name']] = playlist['id']  # Store the playlist name and ID in the dictionary
        print(f"{playlist['name']} - ID: {playlist['id']}")  # Print the playlist name and ID
    return playlist_dict  # Return the dictionary of playlists

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)  # Fetch tracks in the specified playlist
    tracks = results['items']  # Get the initial list of tracks
    while results['next']:  # While there are more tracks to fetch
        results = sp.next(results)  # Fetch the next set of tracks
        tracks.extend(results['items'])  # Add the new tracks to the list
    return tracks  # Return the complete list of tracks

def extract_track_ids(tracks):
    track_ids = []  # Initialize an empty list to store track IDs
    for item in tracks:  # Iterate through each track
        track = item['track']  # Get the track details
        track_ids.append(track['id'])  # Add the track ID to the list
    return track_ids  # Return the list of track IDs

def get_recommendations(track_ids, limit=10):
    recommendations = sp.recommendations(seed_tracks=track_ids[:5], limit=limit)  # Fetch recommendations based on the first 5 track IDs
    return recommendations['tracks']  # Return the recommended tracks

def create_playlist(user_id, name):
    playlist = sp.user_playlist_create(user_id, name, public=False)  # Create a new private playlist
    return playlist['id']  # Return the new playlist ID

def add_tracks_to_playlist(playlist_id, track_ids):
    # Add recommended tracks to the new playlist
    # Track URIs are needed instead of IDs for adding tracks
    track_uris = [f'spotify:track:{track_id}' for track_id in track_ids]
    sp.playlist_add_items(playlist_id, track_uris)

# List all playlists and let the user choose
playlists = list_user_playlists()

# Get tracks from the specified playlist
playlist_id = '6upMS4oCsO6v9ke4Mb4sLf'
tracks = get_playlist_tracks(playlist_id)
track_ids = extract_track_ids(tracks)

# Print the original tracks in the playlist
print("Original Playlist Tracks:")
for idx, item in enumerate(tracks):
    track = item['track']
    print(f"{idx + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

# Get song recommendations based on the extracted track IDs
recommended_tracks = get_recommendations(track_ids)
recommended_track_ids = [track['id'] for track in recommended_tracks]

# Print the recommended tracks
print("\nRecommended Tracks:")
for idx, track in enumerate(recommended_tracks):
    print(f"{idx + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

# Create a new playlist for the recommended tracks
user_id = sp.current_user()['id']  # Get the current user's ID
new_playlist_id = create_playlist(user_id, 'Python Playlist')

# Add recommended tracks to the new playlist
add_tracks_to_playlist(new_playlist_id, recommended_track_ids)

print(f"\nRecommended songs have been added to the new playlist: Recommended Songs")
