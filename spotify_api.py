import base64
import requests
import datetime
from urllib.parse import urlencode
import pprint


CLIENT_ID = 'f970d68b72c642389ed67f78bdecbaa4'
CLIENT_SECRET = 1
CLIENT_CREDS = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode())
TOKEN_URL = 'https://accounts.spotify.com/api/token'
LIMIT_DEFAULT = '1'


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

    """Searching functions"""

    def search_album_by_artist(self, album_name, artist_name):
        pass
        # resp = self.search(query= album_name,

    def search_artist(self, artist_name, limit=LIMIT_DEFAULT):
        resp = self.search(query=artist_name, resource_type='artist',
                           limit=limit)
        genres = resp['artists']['items'][0]['genres']
        info_dict = {'name': resp['artists']['items'][0]['name'],
                     'popularity': resp['artists']['items'][0]['popularity'],
                     'genres': genres}
        return info_dict

    def search(self, query=None, resource_type=None,
               operator=None, operator_query=None, limit=LIMIT_DEFAULT):
        if query is None or resource_type is None:
            raise Exception('Query or resource type not filled')
        if isinstance(query, dict):
            # Puts query in form of a list to be parsed properly in next line
            query_list = [f'{k}:{v}' for k, v in query.items()]
            query = " ".join(query_list)
        if operator is not None and operator_query is not None:
            if operator.lower() == 'or' or operator.lower() == 'not':
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f'{query} {operator} {operator_query}'
        data = urlencode({'q': query, 'type': resource_type.lower(),
                          'limit': f'{limit}'})
        return self.base_search(data)

    def base_search(self, query):
        # Puts query in endpoint; helper function
        endpoint = f'{self.base_url}{self.version}search'
        url_query = f'{endpoint}?{query}'
        resp = requests.get(url_query, headers=self.header)
        if resp.status_code in range(200, 299):
            return resp.json()
        else:
            raise Exception('Issues with given query parameters')

    """Test functions"""
    def run_test_suite(self):
        responses = [
            self.test_token_expiration(),
            self.test_base_search(),
            self.test_search_artist()
        ]
        return print(responses)

    def test_token_expiration(self):
        if self.full_token['access_token'] != '':
            response = 'Token authenticated'
        else:
            response = 'Token not authenticated'
        return print(response)

    def test_base_search(self):
        search_resp = self.search('Danger Zone', 'track')
        danger_zone = 'Danger Zone - From "Top Gun" Original Soundtrack'
        dz_check = search_resp['tracks']['items'][0]['name']
        kenny = 'Kenny Loggins'
        kenny_check = search_resp['tracks']['items'][0]['artists'][0]['name']
        if dz_check == danger_zone and kenny_check == kenny:
            return print('Search functioning')
        else:
            return print('Issue with base_search()')

    def test_search_artist(self):
        search_response = self.search_artist('Kenny Loggins')
        genres = len(search_response['genres'])
        if search_response['name'] == 'Kenny Loggins' and genres == 5:
            return print('Filtering success')
        else:
            raise Exception('Issues with artist_search()')


test = SpotifyAPI()

if __name__ == '__main__':
    test.run_test_suite()
