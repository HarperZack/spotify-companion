import base64
import requests
import datetime
from urllib.parse import urlencode
import pprint


CLIENT_ID = 'f970d68b72c642389ed67f78bdecbaa4'
CLIENT_SECRET = '828f7c6f24be48568803e601d2814d76'
CLIENT_CREDS = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode())
TOKEN_URL = 'https://accounts.spotify.com/api/token'


def now():
    return datetime.datetime.now()


def pp(text):
    return pprint.pprint(text)


class SpotifyAPI:
    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.creds = CLIENT_CREDS
        self.full_token = self.authenticate()
        # Pulls out access token decoded for headers, etc.
        self.access_token = self.full_token['access_token']
        self.is_expired = self.token_expiry()
        self.header = {f'Authorization': f'Bearer {self.access_token}'}
        self.base_url = 'https://api.spotify.com/'
        self.version = 'v1/'

    """Initialization functions"""

    def authenticate(self):
        token_data = {'grant_type': 'client_credentials'}
        token_header = {'Authorization': f'Basic {self.creds.decode()}'}
        r = requests.post(TOKEN_URL, data=token_data, headers=token_header)
        if r.status_code not in range(200, 299):
            raise Exception('Authentication failed')
        return r.json()

    def token_expiry(self):
        expires_in = self.full_token['expires_in']
        expires = datetime.datetime.now() + datetime.timedelta(
            seconds=expires_in)
        return expires < datetime.datetime.now()

    def test_search(self, track='Time'):
        data = urlencode({'q': f'{track}', 'type': 'track'})
        endpoint = f'{self.base_url}{self.version}search'
        url_query = f'{endpoint}?{data}'
        return requests.get(url_query, headers=self.header).json()

    """Searching functions"""

    def get_resource(self, lookup_id, resource_type):
        endpoint = f'{self.base_url}{self.version}{resource_type}/{lookup_id}'
        response = requests.get(endpoint, headers=self.header)
        if response.status_code not in range(200, 299):
            raise Exception('Response failed; check input types')
        return response.json()

    def search_album(self, album_id):
        return self.get_resource(album_id, 'albums')

    def search_artist(self, artist_id):
        return self.get_resource(artist_id, 'artists')

# https://www.youtube.com/watch?v=xdq6Gz33khQ&t=50m40s


t = SpotifyAPI()


def test(tester):
    return print(tester.full_token)


if __name__ == '__main__':
    test(t)
