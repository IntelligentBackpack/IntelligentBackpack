from tinydb import TinyDB, Query, where


class LocalRepositoryImpl:

    def __init__(self, name):
        self.name = name
        self.db = TinyDB(name + '.json')
        self.Tags = Query()

    def addElement(self, value):
        self.db.insert({"tag": value})

    def removeElement(self, value):
        self.db.remove(where('tag') == value)

    def findElement(self, value):
        record = self.db.search(self.Tags.tag == value)
        print(record)
