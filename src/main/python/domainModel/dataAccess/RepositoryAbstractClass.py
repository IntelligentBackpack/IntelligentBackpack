from abc import ABC, abstractmethod


class RepositoryAB(ABC):

    @abstractmethod
    def add_element_into_repository(self, new_tag):
        pass

    @abstractmethod
    def remove_element_into_repository(self, tag):
        pass

    @abstractmethod
    def find_element_into_repository(self, tag):
        pass

    @abstractmethod
    def set_user(self, user):
        pass
