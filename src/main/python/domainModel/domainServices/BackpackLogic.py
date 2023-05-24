# use the policies to add/remove elements into the Backpack retrieved and update db (use cases)
from ..dataAccess.RepositoryAbstractClass import RepositoryAB
from ..policies.InsertNewObjectPolicy import CanInsertNewObject
from ..valueObjects.Book import Book
from ..entities.Backpack import Backpack


class BackpackLogicService:
    def __init__(self, repository: RepositoryAB):
        if isinstance(repository, RepositoryAB):
            # exception
            pass
        self.repository = repository
        self.backpack = Backpack()
        # TODO retrieve username from local db if exist

    def manage_element(self, isbn, tag):
        book = Book(isbn=isbn, tagId=tag)
        if CanInsertNewObject().check_validity(self.repository, self.backpack, book):
            print("AGGIUNGO")
            self.add_element_into_backpack(tag)
        else:
            self.remove_element_into_backpack(tag)

    def add_element_into_backpack(self, value: Book):
        self.repository.add_element_into_repository(value)

    def remove_element_into_backpack(self, value):
        self.repository.remove_element_into_repository(value)

    def find_element_into_backpack(self, value):
        element = self.repository.find_element_into_repository(value)
        return element

    def check_element_missed(self):
        return

    def get_username(self):
        return self.backpack.user_email

    def register(self, user):
        self.backpack.set_user(user)
        self.repository.set_user(user)

    def unregister(self):
        self.backpack.set_user("")
