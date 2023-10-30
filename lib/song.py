class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)



    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] =1

class TestSong:
    def setUp(self):
        from song import Song

    def test_has_song_count(self):
        assert(Song.count == 4)

        ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
        hello = Song("Hello", "Adele", "Pop")
        blank_space = Song("Blank Space", "Taylor Swift", "Pop")
        smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")



print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)



pass
