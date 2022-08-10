from track import Track
import datetime


class Review:
    def __init__(self, track: Track, review_text: str, rating: int):
        if isinstance(track, Track):
            self.__track = track
        else:
            self.__track = None
        if isinstance(review_text, str) and review_text != "":
            self.__review_text = review_text.strip()
        else:
            self.__review_text = "N/A"
        if isinstance(rating, int) and rating > 0 and rating <= 5:
            self.__rating = rating
        else:
            raise ValueError()
        self.__timestamp = datetime.datetime.now()

    @property
    def track(self) -> Track:
        return self.__track

    @property
    def review_text(self) -> str:
        return self.__review_text
    
    @property
    def rating(self) -> int:
        return self.__rating
    
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    
    @track.setter
    def track(self, new_track):
        if isinstance(new_track, Track):
            self.__track = new_track
        else:
            self.__track = None
    
    @review_text.setter
    def review_text(self, new_review_text):
        if isinstance(new_review_text, str) and new_review_text != "":
            self.__review_text = new_review_text.strip()
        else:
            self.__review_text = "N/A"
    
    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, int) and new_rating > 0 and new_rating <= 5:
            self.__rating = new_rating
        else:
            raise ValueError()

    def __repr__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False 
        return self.__track == other.__track and \
        self.__review_text == other.__review_text and \
        self.__rating == other.__rating and \
        self.__timestamp == other.__timestamp 

track1 = Track(2, 'Heat Waves')
review1 = Review(track1, 'very soothing track', 3)
review2 = Review(track1, ' Another review ', 2)
print(review1.track)
print("Review: {}".format(review1.review_text))
print("Rating: {}".format(review1.rating))
