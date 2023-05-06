class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __add__(self, other):
        return Playlist(self.songs + other.songs)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __getitem__(self, index):
        return self.songs[index]

    def __setitem__(self, index, value):
        self.songs[index] = value

    def add_song(self, song):
        self.songs.append(song)


playlist1 = Playlist(["Piosenka 1", "Piosenka 2", "Piosenka 3"])
print(playlist1[0])
playlist1.add_song("Piosenka 4")
print(playlist1.songs)
playlist2 = Playlist(["Piosenka 5", "Piosenka 6"])
playlist3 = playlist1 + playlist2
print(playlist3.songs)
playlist3[1] = "Piosenka 7"
print(playlist3.songs)
