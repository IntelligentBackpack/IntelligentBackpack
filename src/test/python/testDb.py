import unittest
from src.main.python.infrastructureServices.repositories.accessData.LocalRepository import LocalRepositoryImpl


class TestLocalDB(unittest.TestCase):

    def setUp(self):
        self.db = LocalRepositoryImpl("db", "databaseTest.json")

    def tearDown(self):
        self.db.close()

    def test_insertion(self):
        self.db.add_element("123")
        value = self.db.find_element("123")
        self.assertEqual(value, True)

    def test_delete(self):
        self.db.add_element("123")
        self.db.remove_element("123")
        value = self.db.find_element("123")
        self.assertEqual(value, False)

    def test_getElements(self):
        self.db.add_element("123")
        self.db.get_all_tags()
        value = self.db.get_all_tags()
        self.assertEqual(value, ["123"])


if __name__ == '__main__':
    unittest.main()
