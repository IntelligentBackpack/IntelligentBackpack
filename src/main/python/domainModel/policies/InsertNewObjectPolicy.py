from .Policy import PolicyAB
from ..dataAccess.RepositoryAbstractClass import RepositoryAB


class CanInsertNewObject(PolicyAB):

    def __init__(self):
        self = self

    def check_validity(self, repository, value):
        if isinstance(repository, RepositoryAB):
            array = repository.findElementIntoRepository(value)
            if len(array) > 0:
                return False
            else:
                return True
        else:
            return False
