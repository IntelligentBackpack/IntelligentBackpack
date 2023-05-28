from tinydb import TinyDB, Query, where
import json


class LocalRepositoryImpl:
    """
    Class that represents the local database, using the TinyDB framework
    """

    def __init__(self, name, url):
        """
        Constructor method that create the object of this module
            Parameters:
                name (string): The name of the database
                url (string): The local url of the local database in JSON format to create or access

            Returns:
                void
        """
        self.name = name
        self.db = TinyDB(url)
        self.Tags = Query()

    def add_element(self, value):
        """
        Method that add a new element into the database
            Parameters:
                value (string): new value to add into the database

            Returns:
                void
        """
        self.db.insert({"tag": value})

    def remove_element(self, value):
        """
        Method that remove an element from the database
            Parameters:
                value (string): value to be removed from the database

            Returns:
                void
        """
        self.db.remove(where('tag') == value)

    def get_all_tags(self):
        """
        Method that get all the registered values
            Parameters:
                nothing

            Returns:
                records (list): the list of all the registered values
        """
        records = self.db.search(self.Tags.tag.exists())
        return list(map(lambda record: record["tag"], json.loads(json.dumps(records))))

    def find_element(self, value):
        """
        Method that finds the value into the database
            Parameters:
                value (string): tag to find from the repository

            Returns:
                result (boolean): return true if the element is present, false otherwise
        """
        record = self.db.search(where("tag") == value)
        return record != []

    def close(self):
        """
        Method that closes the local database connection
            Parameters:
                nothing

            Returns:
                void
        """
        self.db.close()
