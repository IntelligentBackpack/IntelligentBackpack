# contains all threads to start as static array of singletons
from ...infrastructureServices.modules import RestModule, LedModule, HubIoTModule
from ..dependencyInjection.get_sync_utils import SyncUtils
from ...infrastructureServices.repositories.RepositoryGateway import RepositoryGatewayImpl


def get_remote_db_url():
    """
    Methods that returns the string url of the remote database
    :return: the string url of the remote database
    """
    return "https://intelligentbackpack-d463a-default-rtdb.europe-west1.firebasedatabase.app"


class ServiceLocator:
    """
    Class Service Locator that manage all dependencies and help to performs dependency injection
    """

    def __init__(self):
        """
        Constructor method that initialize all the object dependencies, to be injected in the consumer
        module. The most important dependencies are:
        - HubIotThread to receive messages from cloud
        - NetworkThread to send messages over HTTP protocol
        - RepositoryGateway to manage the databases
        - RFID module
        - and so on
        """
        self.sync_objects = SyncUtils()
        hub_thread = HubIoTModule.HubIotThread(self.sync_objects.queue_messages)
        network_thread = RestModule.NetworkThread("Thread#Network", self.sync_objects.queue_requests)
        network_thread.setDaemon(True)

        self.repository = RepositoryGatewayImpl("db")
        self.repository.set_remote(get_remote_db_url(), self.sync_objects.queue_requests)

        self.modules = [hub_thread, network_thread]

    def get_repository(self):
        """
        Getter method for the repository
        :return: the repository gateway
        """
        return self.repository

    def get_queue(self):
        """
        Getter method for the requests queue
        :return: the requests queue
        """
        return self.sync_objects.queue_requests

    def get_messages_queue(self):
        """
        Getter method for the messages queue
        :return: the messages queue
        """
        return self.sync_objects.queue_messages

    def get_modules(self):
        """
        Getter method for the modules array
        :return: the modules array
        """
        return self.modules