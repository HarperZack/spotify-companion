import spotipy_api as spot
from setlist_creation import setlist_parser
from datetime import datetime
from pprint import pprint as pp

'''
Restricted file needs to contain a Client ID, Secret ID, a Redirect URL, and the path to your Desktop. All of those
(minus the desktop path) are from the Spotify API developer's page.
'''

if __name__ == '__main__':
    # If error of refresh token expired, delete cache and rerun.

    client = spot.SpotifyClient()
    parsed_info = setlist_parser.PlaylistInfo()
    now = datetime.now().strftime('%I:%M:%S %p')

    # Setlist creation function
    client.create_setlist_playlist(parsed_info.playlist_title, parsed_info.queries)
    print(f'{len(parsed_info.queries)} tracks listed.\n')
    if len(parsed_info.extra_tracks) > 0:
        print(f'{len(parsed_info.extra_tracks)} were over the 100 track limit.\n')
    pp(f'Finished at {now}.')


    # Top 50 Playlist and sending function

