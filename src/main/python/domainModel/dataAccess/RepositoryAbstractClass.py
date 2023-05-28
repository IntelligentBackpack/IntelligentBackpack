from abc import ABC, abstractmethod


class RepositoryAB(ABC):
    """
    Abstract class that represents a simple repository, with its basic operations
    """

    @abstractmethod
    def add_element_into_repository(self, new_tag):
        """
        Abstract method that represents the adding of a new element into the database
        :param new_tag: the value to be added
        :return: whatever the client wants
        """
        pass

    @abstractmethod
    def remove_element_into_repository(self, tag):
        """
        Abstract method that represents the removing of an existing element from the database
        :param new_tag: the value to be removed
        :return: whatever the client wants
        """
        pass

    @abstractmethod
    def find_element_into_repository(self, tag):
        """
        Abstract method that represents the finding of an existing element from the database
        :param new_tag: the value to be found
        :return: whatever the client wants
        """
        pass

    @abstractmethod
    def set_user(self, user):
        """
        Abstract method to set the user owner of the repository
        :param user: user to be set
        :return: whatever the client wants
        """
        pass
