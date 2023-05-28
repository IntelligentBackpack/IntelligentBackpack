# Book value object

"""
    Book value object
"""


class Book:
    """
    Class that represents the book value object
    """
    def __init__(self, isbn, tagId):
        """
        Constructor method that initialize a new book object
        :param isbn: isbn code of the book
        :param tagId: tag id of the book
        """
        self.isbn = isbn
        self.tagId = tagId
