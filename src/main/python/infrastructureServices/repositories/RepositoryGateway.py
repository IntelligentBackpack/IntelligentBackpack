from .accessData.LocalRepository import LocalRepositoryImpl
from .accessData.RemoteRepository import RemoteRepositoryImpl
from ...domainModel.dataAccess.RepositoryAbstractClass import RepositoryAB
Repository = RepositoryAB


class RepositoryGatewayImpl(Repository):
    """
    Class that represents the repository gateway, that implements the domain model repository interface.
    Its purpose is to receive all the query to perform into the database, and redirecting them both to the local
    repository database and, if set, to the remote one, transparently
    """

    def __init__(self, name):
        """
        Constructor method that create the object of this module
            Parameters:
                name (string): The name of the database

            Returns:
                void
        """
        self.user = ""
        self.local_repo = LocalRepositoryImpl("db", '../../' + name + '.json')
        self.remote_repo = None

    def set_user(self, user_name):
        """
        Method that set the user owner of this device
            Parameters:
                user_name (string): The name (or email) to set as user owner of the device

            Returns:
                void
        """
        self.user = user_name

    def set_remote(self, url, queue, hash):
        """
        Method that set the remote repository
            Parameters:
                url (string): The url of the remote database where to send the queries
                queue (queue): The queue to use to send the remote requests
                hash (string): The hash that identifies the record on the remote database

            Returns:
                void
        """
        self.remote_repo = RemoteRepositoryImpl(url, queue, hash)

    def sync_remote(self):
        """
        Method that synchronize the remote database with the local one
            Parameters:
                nothing

            Returns:
                void
        """
        if self.remote_repo is not None and self.user != "":
            tags_to_sync = self.local_repo.get_all_tags()
            for tag in tags_to_sync:
                self.remote_repo.add_element(self.user, tag)

    def add_element_into_repository(self, new_tag):
        """
        Method that add a new element into the repository (both local and remote one if set)
            Parameters:
                new_tag (string): new tag to add into the repository

            Returns:
                void
        """
        self.local_repo.add_element(new_tag)
        if self.is_remote_set():
            self.remote_repo.add_element(self.user, new_tag)

    def remove_element_into_repository(self, tag):
        """
        Method that remove an element from the repository (both local and remote one if set)
            Parameters:
                tag (string): tag to remove from the repository

            Returns:
                void
        """
        self.local_repo.remove_element(tag)
        if self.is_remote_set():
            self.remote_repo.remove_element(self.user, tag)

    def find_element_into_repository(self, tag):
        """
        Method that find an element from the repository (both local and remote one if set)
            Parameters:
                tag (string): tag to find from the repository

            Returns:
                result (boolean): return true if the element is present, false otherwise
        """
        local_presence = self.local_repo.find_element(tag)
        return local_presence

    def is_remote_set(self):
        """
        Method that check if the remote database is correctly set
            Parameters:
                nothing

            Returns:
                result (boolean): return true if the remote db is set, false otherwise
        """
        return self.remote_repo is not None

    def close_local(self):
        """
        Method that close the local database connection
            Parameters:
                nothing

            Returns:
                void
        """
        self.local_repo.close()
