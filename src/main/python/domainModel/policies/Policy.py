from abc import ABC, abstractmethod


class PolicyAB(ABC):

    @abstractmethod
    def check_validity(self, *values):
        pass
