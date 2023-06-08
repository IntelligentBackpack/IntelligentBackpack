from .Policy import PolicyAB
from ..dataAccess.RepositoryAbstractClass import RepositoryAB
from ..entities.Backpack import Backpack


class CanInsertNewObject(PolicyAB):
    """
    Policy that checks if a book can be inserted into the backpack
    """

    def __init__(self):
        self = self

    def check_validity(self, repository, backpack: Backpack, book):
        """
        Policy method that checks if a book can be inserted into the backpack
        :param repository: the repository to where check if the element is present
        :param backpack: the backpack to be checked
        :param book: the book to be checked
        :return: true if the book can be inserted, false otherwise
        """
        if backpack.check_book(book):
            return False
        if isinstance(repository, RepositoryAB):
            value = repository.find_element_into_repository(book.tagId)
            if value:
                return False
            else:
                return True
        else:
            return False
