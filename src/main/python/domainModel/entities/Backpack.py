from ..valueObjects.Book import Book
from ..valueObjects.User import User


class Backpack:
    """
    Model entity that represents the backpack
    """

    def __init__(self):
        """
        Constructor method that creates the backpack
        """
        self.id = ""
        self.user = User()
        self.books_lastly_added = []

    def set_user(self, email):
        """
        Method that set the user email of the owner
        :param email: email of the owner
        :return: void
        """
        self.user.email = email
        return

    def get_user(self):
        """
        Method that return the user email of the owner
        """
        return self.user.email

    def set_id(self, id):
        """
        Method that set the user email of the owner
        :param id: id of the backpack
        :return: void
        """
        self.id = id
        return

    def add_book(self, book: Book):
        """
        Method that adds a new book into the backpack
        :param book: book to be added
        :return: void
        """
        self.books_lastly_added.append(book)
        return

    def remove_book(self, book: Book):
        """
        Method that removes an existing book from the backpack
        :param book: the book to be removed
        :return: void
        """
        self.books_lastly_added.remove(book)
        return

    def check_book(self, book: Book):
        """
        Method that checks the existence of the book into the temporary local set of inserted books
        :param book: the book to check
        :return: true if the book is present, false otherwise
        """
        return book in self.books_lastly_added
