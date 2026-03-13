from __future__ import unicode_literals
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from youtubesearchpython import VideosSearch
import youtube_dl

from config import client_id, secret

url = ("https://open.spotify.com/track/3yCKABoZU3FVFuyVBc5VlM?si=8c88f5b4e9eb4569")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

def music(result):
    performers = ""
    music = result['name']
    for names in result["artists"]:
        performers = performers + names["name"] + ", "
    performers = performers.rstrip(", ")
    video = search(music, performers)
    name = f"{performers} - {music}"
    print(name)
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192',}], 'outtmpl': f'./{name}.webm'}
    download(video, ydl_opts)
    print("Готово!")

result = spotify.track(url)
music(result)