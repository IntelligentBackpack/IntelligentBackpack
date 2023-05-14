from tinydb import TinyDB, Query, where
import json

class LocalRepositoryImpl:

    def __init__(self, name):
        self.name = name
        self.db = TinyDB('../../' + name + '.json')
        self.Tags = Query()

    def addElement(self, value):
        self.db.insert({"tag": value})

    def removeElement(self, value):
        self.db.remove(where('tag') == value)

    def getAllTags(self):
        records = self.db.search(self.Tags.tag.exists())
        return list(map(lambda record : record["tag"], json.loads(json.dumps(records))))

    def findElement(self, value):
        record = self.db.search(where("tag") == value)
        return record != []
