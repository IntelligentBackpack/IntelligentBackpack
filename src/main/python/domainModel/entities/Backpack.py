from ..valueObjects.Book import Book


class Backpack:

    def __init__(self):
        self.user_email = ""
        self.books_lastly_added = []

    def set_user(self, email):
        self.user_email = email
        return

    def add_book(self, book: Book):
        self.books_lastly_added.append(book)
        return

    def remove_book(self, book: Book):
        self.books_lastly_added.remove(book)
        return

    def check_book(self, book: Book):
        return book in self.books_lastly_added
