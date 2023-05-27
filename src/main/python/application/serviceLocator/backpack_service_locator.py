# contains all threads to start as static array of singletons
from ...infrastructureServices.modules import RestModule, LedModule, HubIoTModule
from ..dependencyInjection.get_sync_utils import SyncUtils
from ...infrastructureServices.repositories.RepositoryGateway import RepositoryGatewayImpl


def get_remote_db_url():
    return "https://intelligentbackpack-d463a-default-rtdb.europe-west1.firebasedatabase.app"


'''
Class Service Locator that manage all dependencies and help to performs dependency injection
'''
class ServiceLocator:

    def __init__(self):
        self.sync_objects = SyncUtils()
        hub_thread = HubIoTModule.HubIotThread(self.sync_objects.queue_messages)
        network_thread = RestModule.NetworkThread("Thread#Network", self.sync_objects.queue_requests)
        network_thread.setDaemon(True)

        self.repository = RepositoryGatewayImpl("db")
        self.repository.set_remote(get_remote_db_url(), self.sync_objects.queue_requests)

        self.modules = [hub_thread, network_thread]

    def get_repository(self):
        return self.repository

    def get_queue(self):
        return self.sync_objects.queue_requests

    def get_messages_queue(self):
        return self.sync_objects.queue_messages

    def get_modules(self):
        return self.modules