# use the policies to add/remove elements into the Backpack retrieved and update db (use cases)
from ..dataAccess.RepositoryAbstractClass import RepositoryAB
from ..policies.InsertNewObjectPolicy import CanInsertNewObject


class Backpack:
    def __init__(self, repository: RepositoryAB):
        if isinstance(repository, RepositoryAB):
            # exception
            pass
        self.repository = repository

    def addElementIntoBackpack(self, value):
        if CanInsertNewObject().check_validity(self.repository, value):
            self.repository.addElementIntoRepository(value)

    def removeElementIntoBackpack(self, value):
        self.repository.removeElementIntoRepository(value)

    def checkElementMissed(self):
        return
