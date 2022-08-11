import os
import csv
import ast

from domainmodel.track import Track

class TrackCSVReader:
    def __init__(self, albums_csv_file: str, tracks_csv_file: str):
        self.__albums_csv_file = albums_csv_file
        self.__tracks_csv_file = tracks_csv_file

        self.__dataset_of_tracks = []
        # Set of unique artists
        self.__dataset_of_artists = set()
        # Set of unique albums
        self.__dataset_of_albums = set()
        # Set of unique genres
        self.__dataset_of_genres = set()

    @property
    def dataset_of_tracks(self) -> list:
        return self.__dataset_of_tracks

    @property
    def dataset_of_albums(self) -> set:
        return self.__dataset_of_albums

    @property
    def dataset_of_artists(self) -> set:
        return self.__dataset_of_artists

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_files(self):
        with open(self.__tracks_csv_file, encoding="unicode_escape") as file:
            track_file = csv.DictReader(file)
            for line in track_file:
                new_track = Track(int(line["track_id"]), line["track_title"])
                track_artist = Artist(int(line["artist_id"]), line["artist_name"])
                new_track.artist = track_artist
                if line["track_genres"] != "":
                    track_genre_raw_list = ast.literal_eval(line["track_genres"])
                    for genre_entry in track_genre_raw_list:
                        track_genre = Genre(int(genre_entry["genre_id"]), genre_entry["genre_title"])
                        new_track.genres.append(track_genre)
                        self.__dataset_of_genres.add(track_genre)
                new_track.track_duration = int(float(line["track_duration"]))
                new_track.track_duration = int(float(line["track_duration"]))
                new_track.track_url = line["track_url"]
                self.__dataset_of_tracks.append(new_track)
                self.__dataset_of_artists.add(track_artist)
                
        with open(self.__albums_csv_file, encoding="unicode_escape") as file:
            album_file = csv.DictReader(file)
            for line in album_file:
                new_album = Album(int(line["album_id"]), line["album_title"])
                self.__dataset_of_albums.add(new_album)


albums_file_name = 'CS235_S2_2022-Assignment1-CodeSkeleton\data\raw_albums_excerpt.csv'
tracks_file_name = 'CS235_S2_2022-Assignment1-CodeSkeleton\data\raw_tracks_excerpt.csv'
reader = TrackCSVReader(albums_file_name, tracks_file_name)
reader.read_csv_files()

print(f'number of unique tracks: {len(reader.dataset_of_tracks)}')
print(f'number of unique artists: {len(reader.dataset_of_artists)}')
print(f'number of unique albums: {len(reader.dataset_of_albums)}')
print(f'number of unique genres: {len(reader.dataset_of_genres)}')

