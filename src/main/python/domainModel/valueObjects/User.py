"""
    User value object
"""


class User:
    """
    Class that represents the user value object
    """
    def __init__(self, username="", surname="", email=""):
        """
        Constructor method that initialize a new user
        :param username: username of the user
        :param surname: surname of the user
        :param email: email of the user
        """
        self.username = username
        self.surname = surname
        self.email = email
