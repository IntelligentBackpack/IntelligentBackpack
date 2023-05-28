from abc import ABC, abstractmethod


class PolicyAB(ABC):
    """
    Abstract class that represents a simple policy, with its basic check validity operation
    """

    @abstractmethod
    def check_validity(self, *values):
        """
        Abstract method that check a simple policy validity
        :param values: the value to check
        :return: the boolean response based on a specific policy
        """
        pass
