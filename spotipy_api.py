import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = 'b548bbde8d88420aa1b7229742ebcd2a'
CLIENT_SECRET = '863dd96c91f1428ca2d869b2c7097620'
SCOPE = [
    'user-library-read'
]


class SpotifyClient:
    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

    def viability_check(self):
        pass

