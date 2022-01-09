import spotipy_api as spot
import setlist_parser
from datetime import datetime
import os
#
# spotify = spotify_api.SpotifyAPI


if __name__ == '__main__':
    # Check app's authorization and accuracy
    client = spot.SpotifyClient()

    parsed_info = setlist_parser.PlaylistInfo()
    searches = parsed_info.queries
    title = parsed_info.playlist_title
    now = datetime.now().strftime('%I:%M:%S %p')

    print(title)
    print(searches)
    print(now)

