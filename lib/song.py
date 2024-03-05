class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
       super().__init__()
       self.name = name
       self.artist = artist
       self.genre = genre

       self.__class__.count += 1
       self.__class__.genres.append(genre)
       self.__class__.artists.append(artist)

       if genre not in self.__class__.genre_count:
            self.__class__.genre_count[genre] = 1
       else:
            self.__class__.genre_count[genre] += 1

       if artist not in self.__class__.artist_count:
            self.__class__.artist_count[artist] = 1
       else:
            self.__class__.artist_count[artist] += 1

       self.__class__.genres = list(set(self.__class__.genres))
       self.__class__.artists = list(set(self.__class__.artists))

    @classmethod
    def add_to_genres(cls):
        genre = cls.genre
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls):
        artist = cls.artist
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        if not cls.genre_count:
            for genre in cls.genres:
                cls.genre_count[genre] = 1
        else:
            for genre in cls.genres:
                if genre not in cls.genre_count:
                    cls.genre_count[genre] = 1
                else:
                    cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls):
     for artist in cls.artists:
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

pass

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
standing_next_to_you = Song("Standing next to you", "jungkook", "kpop")
save_your_tears = Song("save your tears", "the weekend", "rnb")

print(ninety_nine_problems.name, ninety_nine_problems.artist, ninety_nine_problems.genre) 
print(Song.count, Song.genres, Song.artists, Song.artist_count, Song.genre_count)

print(standing_next_to_you.name, standing_next_to_you.artist, standing_next_to_you.genre)
print(Song.count, Song.genres, Song.artists, Song.artist_count, Song.genre_count)

print(save_your_tears.name, save_your_tears.artist , save_your_tears.genres)
print(Song.count, Song.genres, Song.artists, Song.artist_count, Song.genre_count)
