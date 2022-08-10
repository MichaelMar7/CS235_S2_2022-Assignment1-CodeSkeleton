class Genre:
    def __init__(self, genre_id: int, genre_name: str):
        if not isinstance(genre_id, int) or genre_id < 0:
            raise ValueError("Invalid id.")
        self.__genre_id: int = genre_id
        try:
            self.__genre_name = genre_name.strip()
        except:
            self.__genre_name = None

    @property
    def genre_id(self) -> int:
        return self.__genre_id

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def name(self, new_genre_name):
        try:
            self.__genre_name = new_genre_name.strip()
        except:
            self.__genre_name = None

    def __repr__(self):
        # we use access via the property here
        return f"<Genre {self.genre_name}, genre id = {self.genre_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id == other.genre_id

    def __lt__(self, other):
        return self.genre_id < other.genre_id

    def __hash__(self):
        return hash(self.genre_id)


genre1 = Genre(1, 'Jazz ')
print(genre1)
genre2 = Genre(2, ' Electronic ')
print(genre2)
genre3 = Genre(3, 300)
print(genre3.name)
genre4 = Genre(1, 'Jazz')
genre4.name = 'New Jazz'
print(genre4)

