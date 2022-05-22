

class Song:

    def __init__(self, artist, name, key, tempo, camelot) -> None:
        self.artist = artist
        self.name = name
        self.key = key
        self.tempo = tempo
        self.camelot = camelot
    
    def toString(self):
        return self.artist + ": " + self.name