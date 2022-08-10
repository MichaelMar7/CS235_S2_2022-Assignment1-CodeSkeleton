from artist import Artist
from genre import Genre
from album import Album

class Track:
    def __init__(self, track_id : int, title: str):
        if not isinstance(track_id , int) or track_id  < 0:
            raise ValueError("Invalid id.")
        self.__track_id  = track_id 
        try:
            if not isinstance(title, str) or title == "":
                raise Exception()
            self.__title = title.strip()
        except:
            self.__title = None
        self.__album = None
        self.__artist = None
        self.__genres = []
        self.__track_duration = 0
        self.__track_url = None

    @property
    def track_id(self) -> int:
        return self.__track_id 

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def album(self) -> Album:
        return self.__album

    @property
    def artist(self) -> Artist:
        return self.__artist
    
    @property
    def genres(self) -> list:
        return self.__genres
    
    @property
    def track_duration(self) -> int:
        return self.__track_duration
    
    @property
    def track_url(self) -> str:
        return self.__track_url
    
    @title.setter
    def title(self, new_title):
        try:
            if not isinstance(new_title, str) or new_title == "":
                raise Exception()
            self.__title = new_title.strip()
        except:
            self.__title = None
    
    @album.setter
    def album(self, new_album):
        try:
            if not isinstance(new_album, Album):
                raise Exception()
            self.__album = new_album
        except:
            self.__album = None
    
    @artist.setter
    def artist(self, new_artist):
        try:
            if not isinstance(new_artist, Artist):
                raise Exception()
            self.__artist = new_artist
        except:
            self.__artist = None

    @track_duration.setter
    def track_duration(self, new_track_duration):
        if not isinstance(new_track_duration, int) or new_track_duration < 0:
            raise ValueError()
        self.__track_duration = new_track_duration
    
    @artist.setter
    def track_url(self, new_track_url):
        try:
            if not isinstance(new_track_url, str) or new_track_url == "":
                raise Exception()
            self.__track_url = new_track_url.strip()
        except:
            self.__track_url = None

    def add_genre(self, new_genre):
        if isinstance(new_genre, Genre):
            self.__genres.add(new_genre)

    def __repr__(self):
        # we use access via the property here
        return f"<Track {self.__title}, track id = {self.__track_id }>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__track_id  == other.__track_id 

    def __lt__(self, other):
        return self.__track_id  < other.__track_id 

    def __hash__(self):
        return hash(self.__track_id)

track1 = Track(1, 'As it Was ')
print(track1)
track2 = Track(2, ' Heat Waves')
print(track2)
track3 = Track(3, ' Tarot ')
print(track3)
track4 = Track(5, 32)
print(track4.title) 

trackList = []
trackList.append(track2)
trackList.append(track4)
trackList.append(track3)
trackList.append(track1)
trackList.sort()
trackList.pop(2)
print(trackList)


