import spotipy_api as spot
import setlist_parser
from datetime import datetime
from pprint import pprint as pp

if __name__ == '__main__':
    client = spot.SpotifyClient()
    parsed_info = setlist_parser.PlaylistInfo()
    now = datetime.now().strftime('%I:%M:%S %p')

    # Setlist creation function
    client.create_setlist_playlist(parsed_info.playlist_title, parsed_info.queries)
    pp(f'{len(parsed_info.queries)} tracks listed.')
    pp(now)

    # Top 50 Playlist and sending function

