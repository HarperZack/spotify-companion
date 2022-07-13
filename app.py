import spotipy_api
import spotipy_api as spot
import setlist_parser
from datetime import datetime


if __name__ == '__main__':
    # Check app's authorization and accuracy
    client = spot.SpotifyClient()
    test = spotipy_api.Tests()

    if test.run() is True:
        parsed_info = setlist_parser.PlaylistInfo()
        searches = parsed_info.queries
        title = parsed_info.playlist_title
        now = datetime.now().strftime('%I:%M:%S %p')

        print(title)
        print(searches)
        print(now)
    else:
        print('Check test class')

    client.search_track('billie jean')
