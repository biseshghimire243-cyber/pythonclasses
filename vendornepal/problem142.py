class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def show(self):

        print(
            self.title,
            "-",
            self.artist
        )


class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):

        self.songs.append(song)

        print("Song added.")

    def remove_song(self, title):

        for song in self.songs:

            if song.title.lower() == title.lower():

                self.songs.remove(song)

                print("Song removed.")
                return

        print("Song not found.")

    def show_playlist(self):

        print(
            "\n==========",
            self.name,
            "=========="
        )

        if not self.songs:

            print("Playlist is empty.")
            return

        for number, song in enumerate(
            self.songs,
            start=1
        ):

            print(
                number,
                end=". "
            )

            song.show()


playlist = Playlist("My Python Playlist")

playlist.add_song(
    Song("Perfect", "Ed Sheeran")
)

playlist.add_song(
    Song("Believer", "Imagine Dragons")
)

playlist.add_song(
    Song("Shape of You", "Ed Sheeran")
)

playlist.show_playlist()

playlist.remove_song("Believer")

playlist.show_playlist()