# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:  # Define a class named 'Book'

    def __init__(self, name: str, author: str, genre: str, year: int):  # Class constructor to initialize attributes
        self.name = name  # 'name' attribute to store book name
        self.author = author  # 'author' attribute to store book author
        self.genre = genre  # 'genre' attribute to store book genre
        self.year = year  # 'year' attribute to store book publication year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):  # Customized string representation method
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"  # Returns formatted book information

    # -----------------------------
    # Write your solution here
    # -----------------------------

    def books_of_genre(books: list, genre: str):  # Define a function named 'books_of_genre'
        book_genre = []  # Create an empty list to store books of the specified genre

        for book in books:  # Iterate through the 'books' list
            if book.genre == genre:  # Check if the current book's genre matches the 'genre' parameter
                book_genre.append(book)  # Add the book to the 'book_genre' list if it matches the genre
        return book_genre  # Return the list of books of the specified genre
