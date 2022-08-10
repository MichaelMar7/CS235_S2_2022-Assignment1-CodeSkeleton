class Album:
    def __init__(self, album_id: int, title: str):
        if not isinstance(album_id, int) or album_id < 0:
            raise ValueError("Invalid id.")
        self.__album_id = album_id
        try:
            if not isinstance(title, str) or title == "":
                raise Exception()
            self.__title = title.strip()
        except:
            self.__title = None
        self.__album_url = None
        self.__album_type = None
        self.__release_year = None

    @property
    def album_id(self) -> int:
        return self.__album_id

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def album_url(self) -> int:
        return self.__album_url

    @property
    def album_type(self) -> str:
        return self.__album_type
    
    @property
    def release_year(self) -> int:
        return self.__release_year
    
    @title.setter
    def title(self, new_title):
        try:
            if not isinstance(new_title, str) or new_title == "":
                raise Exception()
            self.__title = new_title.strip()
        except:
            self.__title = None
    
    @album_url.setter
    def album_url(self, new_album_url):
        try:
            if not isinstance(new_album_url, str) or new_album_url == "":
                raise Exception()
            self.__album_url = new_album_url.strip()
        except:
            self.__album_url = None
    
    @album_type.setter
    def album_type(self, new_album_type):
        try:
            if not isinstance(new_album_type, str) or new_album_type == "":
                raise Exception()
            self.__album_type = new_album_type.strip()
        except:
            self.__album_type = None

    @release_year.setter
    def release_year(self, new_release_year):
        if not isinstance(new_release_year, int) or new_release_year < 0:
            raise ValueError("Invalid id.")
        self.__release_year = new_release_year

    def __repr__(self):
        # we use access via the property here
        return f"<Album {self.__title}, album id = {self.__album_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__album_id == other.__album_id

    def __lt__(self, other):
        return self.__album_id < other.__album_id

    def __hash__(self):
        return hash(self.__album_id)

album1 = Album(15, 'Justice')
print(album1)
album2 = Album(20, '')
print(album2)
album3 = Album(20, ' Planet Her ')
print(album3)
album4 = Album(3, 300)
print(album4)
