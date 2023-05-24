from .accessData.LocalRepository import LocalRepositoryImpl
from .accessData.RemoteRepository import RemoteRepositoryImpl
from ...domainModel.dataAccess.RepositoryAbstractClass import RepositoryAB
Repository = RepositoryAB


class RepositoryGatewayImpl(Repository):

    def __init__(self, name):
        self.user = ""
        self.local_repo = LocalRepositoryImpl("db", '../../' + name + '.json')
        self.remote_repo = None

    def set_user(self, user_name):
        self.user = user_name

    def set_remote(self, url, queue):
        # TODO gestire hash
        self.remote_repo = RemoteRepositoryImpl(url, queue, "hash")

    def sync_remote(self):
        if self.remote_repo is not None:
            tags_to_sync = self.local_repo.get_all_tags()
            for tag in tags_to_sync:
                self.remote_repo.add_element(self.user, tag)

    def add_element_into_repository(self, new_tag):
        self.local_repo.add_element(new_tag)
        if self.is_remote_set():
            self.remote_repo.add_element(self.user, new_tag)

    def remove_element_into_repository(self, tag):
        self.local_repo.remove_element(tag)
        if self.is_remote_set():
            self.remote_repo.remove_element(self.user, tag)

    def find_element_into_repository(self, tag):
        local_presence = self.local_repo.find_element(tag)
        return local_presence

    def is_remote_set(self):
        return self.remote_repo is not None

    def close_local(self):
        self.local_repo.close()
