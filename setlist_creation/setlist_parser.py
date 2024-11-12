import os
import restricted

TEXT_FILE = os.path.join(restricted.DESKTOP, 'Setlist to Playlist.txt')


class PlaylistInfo:
    def __init__(self):
        self.queries = list()
        self.playlist_title = str()
        self.track_count = 0
        self.extra_tracks = list()
        self.parse_text_file()

    def parse_text_file(self):
        with open(TEXT_FILE, 'r') as source:
            for line in source:
                line = line.strip()
                if '\'' in line:
                    line.replace('\'', '')
                if '\"' in line:
                    line.replace('\"', "")
                if line != '':
                    self.queries.append(line)
            self.playlist_title = self.queries[0]
            del self.queries[0]

            self.track_count = len(self.queries)

            if self.track_count > 100:
                self.extra_tracks = self.queries[100:]
                del self.queries[100:]

