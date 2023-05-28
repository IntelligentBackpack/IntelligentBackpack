import unittest
from src.main.python.domainModel.entities.Backpack import Backpack
from src.main.python.domainModel.valueObjects.Book import Book


class TestBackpack(unittest.TestCase):

    def setUp(self):
        self.backpack = Backpack()

    def test_set_user(self):
        email = "daniele.dilillo@email.com"
        self.backpack.set_user("daniele.dilillo@email.com")
        value = self.backpack.user_email
        self.assertEqual(value, email)

    def test_add_book(self):
        book = Book("nameBook", "123", "5")
        self.backpack.add_book(book)
        value = self.backpack.check_book(book)
        self.assertEqual(value, True)

    def test_remove_book(self):
        book = Book("nameBook", "123", "5")
        self.backpack.add_book(book)
        self.backpack.remove_book(book)
        value = self.backpack.check_book(book)
        self.assertEqual(value, False)


if __name__ == '__main__':
    unittest.main()
