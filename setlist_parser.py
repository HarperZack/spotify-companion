import os

DESKTOP = os.path.join('C:', os.sep, 'Users', 'Zack', 'Desktop')
TEXT_FILE = os.path.join(DESKTOP, 'Setlist to Playlist.txt')


class PlaylistInfo:
    def __init__(self):
        self.queries = list()
        self.playlist_title = str()
        self.parse_text_file()

    def parse_text_file(self):
        with open(TEXT_FILE, 'r') as source:
            for line in source:
                line = line.strip()
                if '\'' in line:
                    line.replace('\'', '')
                if line != '':
                    self.queries.append(line)
            self.playlist_title = self.queries[0]
            del self.queries[0]
