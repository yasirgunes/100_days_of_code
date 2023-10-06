import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import re

scope = "user-library-read playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

user_id = sp.current_user()['id']

################################################################################################

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
response.raise_for_status()
content = response.text

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} HOT 100", public=True)["id"]

soup = BeautifulSoup(content, "html.parser")
songs = [re.sub(r'[\n\t]', '', item.get_text()) for item in soup.select(selector="li h3#title-of-a-story")]
song_uris = []
song_number: int = 1
for song in songs:
    results = sp.search(q=f"track:{song} year:{date.split('-')[0]}", limit=1, type="track")
    print(f"Adding the {song_number}. song...")
    song_number += 1
    if len(results['tracks']['items']) > 0:
        track_uri = results['tracks']['items'][0]['uri']  # Use the URI of the first search result
        song_uris.append(track_uri)
    else:
        print("Song not found.")

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
