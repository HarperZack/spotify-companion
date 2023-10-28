import spotipy
from pprint import pprint as pp

REDIRECT = 'http://127.0.0.1:9090'
CLIENT_ID = 'b548bbde8d88420aa1b7229742ebcd2a'
CLIENT_SECRET = '47def98fdcec48a1af068cdb5a1ba48d'
SCOPE = [
    'user-library-read',
    'playlist-modify-public'
]


class SpotifyClient:
    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, scope=SCOPE,
                                                                               redirect_uri=REDIRECT))
        self.me = self.client.me()['id']
    """
    Helper Methods for track searching
    """
    def get_name(self, results):
        return results['tracks']['items'][0]['name']

    def get_artist(self, results):
        return results['tracks']['items'][0]['artists'][0]['name']

    def get_track_uri(self, results):
        return results['tracks']['items'][0]['uri']

    """
    Searching methods
    """
    def search_track(self, name):
        results = self.client.search(name)
        pp(self.get_name(results))
        return self.get_track_uri(results)

    def search_artist(self, name):
        results = self.client.search(name)
        return self.get_artist(results)

    """
    Playlist Methods
    """
    def create_playlist(self, title):
        self.client.user_playlist_create(user=self.me, name=title)
        pp(f'Created playlist {title}.')
        playlists = self.client.user_playlists(user=self.me)
        return playlists['items'][0]['id']

    def add_to_playlist(self, playlist_title, songs):
        tracks = list()
        for song in songs:
            tracks.append(self.search_track(song))
        self.client.playlist_add_items(playlist_title, tracks)

    """
    Main creation methods
    """
    def create_setlist_playlist(self, playlist_title, tracks):
        if len(tracks) <= 100:
            playlist_id = self.create_playlist(playlist_title)
            self.add_to_playlist(playlist_id, tracks)

            '''
            Some function here to grab the second list of songs and add them in another call to get around 100 track
            limit per request. Not sure what a request is considered, but if its just another function call, I'm set
            '''


