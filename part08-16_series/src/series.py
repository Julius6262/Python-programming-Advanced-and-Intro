import numpy as np
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rate_list = []

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.rate_list.append(rating)
    
    # Helper method
    def genres_str(self):
        return ", ".join(self.genres)
    
    #Helper method
    def rating_values(self):
        if self.rate_list:
            return (len(self.rate_list), (np.mean(self.rate_list)))
        else:
            return ("no ratings", "no ratings")
    
    def __str__(self):      
        line_1 = f"{self.title} ({self.seasons} seasons)"
        line_2 = f"genres: {self.genres_str()}"
        
        if len(self.rate_list) > 0:
            rating_count, avg_rating = self.rating_values()  # Call rating_values method
            line_3 = f"{rating_count} ratings, average {avg_rating:.1f} points"
        else:
            line_3 = "no ratings"
        return f"{line_1}\n{line_2}\n{line_3}"



def minimum_grade(rating:float, series_list: list):
    minimum_list = []
    for series in series_list:
        if series.rating_values()[1] >= rating:
            minimum_list.append(series)
    return minimum_list

def includes_genre(genre: str, series_list: list):
    genres_list = []
    for series in series_list:
        if genre in series.genres:
            genres_list.append(series)
    return genres_list
