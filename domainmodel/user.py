from track import Track
from review import Review

class User:
    def __init__(self, user_id: int, user_name: str, password: str):
        if isinstance(user_id, int) and user_id >= 0:
            self.__user_id = user_id
        else:
            raise ValueError()
        if isinstance(user_name, str) and user_name != "":
            self.__user_name = user_name.strip().lower()
        else:
            self.__user_name = None
        if isinstance(password, str) and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None
        self.__liked_tracks = []
        self.__reviews = []
    
    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def liked_tracks(self) -> list:
        return self.__liked_tracks

    @property
    def reviews(self) -> list:
        return self.__reviews
    
    def __repr__(self):
        return f"<User {self.__user_name}, user id = {self.__user_id }>"
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False 
        return self.__user_id == other.__user_id
    
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False 
        return self.__user_id < other.__user_id
    
    def __hash__(self):
        return hash(self.__user_id)
    
    def add_liked_track(self, track):
        if isinstance(track, Track) and track not in self.__liked_tracks:
            self.__liked_tracks.append(track)
    
    def remove_liked_track(self, track):
        if track in self.__liked_tracks:
            self.__liked_tracks.remove(track)
    
    def add_review(self, review):
        if isinstance(review, Review) and review not in self.__reviews:
            self.__reviews.append(review)
    
    def remove_review(self, review):
        if review in self.__reviews:
            self.__reviews.remove(review)

user1 = User(123, 'Shyamli', 'pw12345')
user2 = User(345, 'asma', 'pw67890')
user3 = User(567, 'Daniel', 'pw87465')
print(user1)
print(user2)
print(user3)

track1 = Track(2, 'Heat Waves')
review1 = Review(track1, 'very soothing track', 3)
user1.add_review(review1)
user1.add_review(review1)
user1.remove_review(review1)
print(type(user1.reviews))
