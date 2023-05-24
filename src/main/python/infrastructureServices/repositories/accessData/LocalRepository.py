from tinydb import TinyDB, Query, where
import json


class LocalRepositoryImpl:

    def __init__(self, name, url):
        self.name = name
        self.db = TinyDB(url)
        self.Tags = Query()

    def add_element(self, value):
        self.db.insert({"tag": value})

    def remove_element(self, value):
        self.db.remove(where('tag') == value)

    def get_all_tags(self):
        records = self.db.search(self.Tags.tag.exists())
        return list(map(lambda record: record["tag"], json.loads(json.dumps(records))))

    def find_element(self, value):
        record = self.db.search(where("tag") == value)
        return record != []

    def close(self):
        self.db.close()
