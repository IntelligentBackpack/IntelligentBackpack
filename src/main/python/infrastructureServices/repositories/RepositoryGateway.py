from .accessData.LocalRepository import LocalRepositoryImpl
from ...domainModel.dataAccess.RepositoryAbstractClass import RepositoryAB
Repository = RepositoryAB


class RepositoryGatewayImpl(Repository):

    def __init__(self):
        self.localRepo = LocalRepositoryImpl("db")

    def addElementIntoRepository(self, newTag):
        self.localRepo.addElement(newTag)

    def removeElementIntoRepository(self, tag):
        self.localRepo.removeElement(tag)

    def findElementIntoRepository(self, tag):
        self.localRepo.findElement(tag)

# repo = RepositoryGateway()
# repo.addElementIntoRepository("123456789")
# repo.removeElementIntoRepository("123456789")
# repo.findElementIntoRepository("123456789")
