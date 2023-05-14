from .accessData.LocalRepository import LocalRepositoryImpl
from .accessData.RemoteRepository import RemoteRepositoryImpl
from ...domainModel.dataAccess.RepositoryAbstractClass import RepositoryAB
Repository = RepositoryAB

class RepositoryGatewayImpl(Repository):
    #TODO fare una factory??
    def __init__(self, url, queue):
        self.localRepo = LocalRepositoryImpl("db")
        self.remoteRepo = RemoteRepositoryImpl(url, queue)
        tags_to_sync = self.localRepo.getAllTags()
        for tag in tags_to_sync:
            self.remoteRepo.addElement(tag)

    def addElementIntoRepository(self, newTag):
        self.localRepo.addElement(newTag)
        self.remoteRepo.addElement(newTag)

    def removeElementIntoRepository(self, tag):
        self.localRepo.removeElement(tag)
        self.remoteRepo.removeElement(tag)

    def findElementIntoRepository(self, tag):
        localPresence = self.localRepo.findElement(tag)
        remotePresence = self.remoteRepo.findElement(tag)
        return localPresence or remotePresence
