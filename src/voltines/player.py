import webbrowser
from .data import YOUTUBE_PLAYLIST_URL


def watch(song: str):
    print(f"Attempting to open performance of: {song}")
    webbrowser.open(YOUTUBE_PLAYLIST_URL)
