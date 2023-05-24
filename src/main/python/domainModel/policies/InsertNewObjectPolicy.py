from .Policy import PolicyAB
from ..dataAccess.RepositoryAbstractClass import RepositoryAB
from ..entities.Backpack import Backpack


class CanInsertNewObject(PolicyAB):

    def __init__(self):
        self = self

    def check_validity(self, repository, backpack: Backpack, book):
        if backpack.check_book(book):
            return False
        if isinstance(repository, RepositoryAB):
            value = repository.find_element_into_repository(book)
            if value:
                return False
            else:
                return True
        else:
            return False
