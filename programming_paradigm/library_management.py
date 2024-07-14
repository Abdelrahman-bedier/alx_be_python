
class Book:
    def __init__(self, title, author):
        self.__is_checked_out = False
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_checked_out(self):
        return self.__is_checked_out
    
    def check_out(self):
        self.__is_checked_out = True
    
    def return_book(self):
        self.__is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, Book):
        self._books.append(Book)
    
    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                book.check_out()
                break

    def return_book(self, title):
        for book in self._books:
            if title == book.title:
                book.return_book()