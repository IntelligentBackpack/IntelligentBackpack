from abc import ABC, abstractmethod


class RepositoryAB(ABC):

    @abstractmethod
    def addElementIntoRepository(self, newTag):
        pass

    @abstractmethod
    def removeElementIntoRepository(self, tag):
        pass

    @abstractmethod
    def findElementIntoRepository(self, tag):
        pass
