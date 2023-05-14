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

    def manageElement(self, isbn, tag):
        book = Book(isbn=isbn, tagId=tag)
        if CanInsertNewObject().check_validity(self.repository, self.backpack, book):
            self.addElementIntoBackpack(tag)
        else:
            self.removeElementIntoBackpack(tag)

    def addElementIntoBackpack(self, value: Book):
        self.repository.addElementIntoRepository(value)

    def removeElementIntoBackpack(self, value):
        self.repository.removeElementIntoRepository(value)

    def findElementIntoBackpack(self, value):
        element = self.repository.findElementIntoRepository(value)
        return element

    def checkElementMissed(self):
        return
