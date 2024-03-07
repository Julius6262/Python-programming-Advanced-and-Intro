# Write your solution here
def find_movies(database: list, search_term: str):
    new_list = []
    for movie in database:
        name = movie.get("name")
        if search_term.lower() in name.lower():
            new_list.append(movie)
    return new_list
