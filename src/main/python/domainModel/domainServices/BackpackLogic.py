# use the policies to add/remove elements into the Backpack retrieved and update db (use cases)
from ..dataAccess.RepositoryAbstractClass import RepositoryAB
from ..policies.InsertNewObjectPolicy import CanInsertNewObject
from ..valueObjects.Book import Book
from ..entities.Backpack import Backpack


class BackpackLogicService:
    """
    Domain logic service that models the operations that can be performed to the
    backpack
    """

    def __init__(self, repository: RepositoryAB):
        """
        Constructor method that initialize the backpack
        :param repository: the repository to use
        """
        if isinstance(repository, RepositoryAB):
            pass
        self.repository = repository
        self.backpack = Backpack()

    def manage_element(self, isbn, tag):
        """
        Entry method that manage a new book that the backpack did read
        :param isbn: isbn value of the book
        :param tag: tag value of the book/object
        :return: void
        """
        book = Book(isbn=isbn, tagId=tag)
        if CanInsertNewObject().check_validity(self.repository, self.backpack, book):
            self.add_element_into_backpack(tag)
        else:
            self.remove_element_into_backpack(tag)

    def add_element_into_backpack(self, value: Book):
        """
        Method that add a new element into the backpack
        :param value: the value to be added
        :return: void
        """
        self.repository.add_element_into_repository(value)

    def remove_element_into_backpack(self, value):
        """
        Method that remove an existing element from the backpack
        :param value: the value to be added
        :return: void
        """
        self.repository.remove_element_into_repository(value)

    def find_element_into_backpack(self, value):
        """
        Method that finds an existing element from the backpack
        :param value: the value to be found
        :return: void
        """
        element = self.repository.find_element_into_repository(value)
        return element

    def get_username(self):
        """
        Getter method that returns the username of the owner
        :return: the user email or name
        """
        return self.backpack.user_email

    def set_id(self, id):
        """
        Method that register the user owner
        :param user: the username string
        :return: none
        """
        self.backpack.set_id(id)

    def register(self, user):
        """
        Method that register the user owner
        :param user: the username string
        :return: none
        """
        self.backpack.set_user(user)
        self.repository.set_user(user)

    def unregister(self):
        """
        Method that unregister the user
        :return: none
        """
        self.backpack.set_user("")
        self.repository.set_user(None)
