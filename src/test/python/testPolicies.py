import unittest
from src.main.python.domainModel.entities.Backpack import Backpack
from src.main.python.domainModel.valueObjects.Book import Book
from src.main.python.domainModel.policies.InsertNewObjectPolicy import CanInsertNewObject
from src.main.python.infrastructureServices.factories.RepositoryFactory import local_repository_gateway


class TestBackpack(unittest.TestCase):

    def setUp(self):
        self.backpack = Backpack()
        self.repo = local_repository_gateway("db")
        self.canInsertNewObject = CanInsertNewObject()

    def tearDown(self):
        self.repo.close_local()

    def test_check_validity_empty(self):
        book = Book("nameBook", "123", "5")
        value = self.canInsertNewObject.check_validity(self.repo, self.backpack, book)
        self.assertEqual(value, True)

    def test_check_validity_full(self):
        book = Book("nameBook", "123", "5")
        self.backpack.add_book(book)
        value = self.canInsertNewObject.check_validity(self.repo, self.backpack, book)
        self.assertEqual(value, False)


if __name__ == '__main__':
    unittest.main()
