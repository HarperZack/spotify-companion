import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

CLIENT_ID = 'b548bbde8d88420aa1b7229742ebcd2a'
CLIENT_SECRET = '863dd96c91f1428ca2d869b2c7097620'
SCOPE = [
    'user-library-read'
]


class SpotifyClient:
    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

    """
    Helper Methods for track searching
    """
    def get_name(self, results):
        return results['tracks']['items'][0]['name']

    def get_artist(self, results):
        return results['tracks']['items'][0]['artists'][0]['name']

    def search_track(self, name):
        results = self.client.search(name)
        pprint(self.get_name(results))

    def search_artist(self, name):
        results = self.client.search(name)
        pprint(self.get_artist(results))


class Tests:
    def __init__(self):
        self.client = SpotifyClient()
        self.Billy_Joel = 'Billie Joel'
        self.Billy_Shears = 'With a Little Help From My Friends'
        self.Billy_Joe = 'Green Day'
        self.Billie_Jean = 'Billie Jean'

    def run(self):
        if self.client.get_name(self.Billie_Jean) is self.Billie_Jean:
            if self.client.get_name(self.Billy_Shears) is self.Billy_Shears:
                if self.client.get_artist(self.Billy_Joel) is self.Billy_Joel:
                    if self.client.get_artist(self.Billy_Joe) == 'Green Day':
                        return True
        else:
            return False

