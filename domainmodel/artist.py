class Artist:
    def __init__(self, artist_id: int, full_name: str):
        if not isinstance(artist_id, int) or artist_id < 0:
            raise ValueError("Invalid id.")
        self.__artist_id: int = artist_id
        try:
            if full_name == "":
                raise Exception()
            self.__full_name = full_name.strip()
        except:
            self.__full_name = None

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        try:
            self.__full_name = new_full_name.strip()
        except:
            self.__full_name = None

    def __repr__(self):
        # we use access via the property here
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        return self.artist_id < other.artist_id

    def __hash__(self):
        return hash(self.artist_id)

# Test
artist1 = Artist(1, 'Tailor Swift')
print(artist1)
artist2 = Artist(2, "Maroon 5")
artist2.full_name = 32
print(artist2)
artist3 = Artist(3, 'Kate Bush')
print(artist3)
artist4 = Artist(4, ' Bad Bunny ')
print(artist4)
artist5 = Artist(5, 2910)
print(artist5.full_name)

print()
"""
artist6 = Artist("sixtynine", "Michael Mar") # id not int
print(artist6)
artist7 = Artist(-1, "Michael Mar") # id negative
print(artist7)
"""

artistList = [artist3, artist1, artist5, artist4, artist2]
artistList.sort()
print(artistList)
