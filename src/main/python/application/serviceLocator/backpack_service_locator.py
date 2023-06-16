# contains all threads to start as static array of singletons
from ...infrastructureServices.modules import RestModule, HubIoTModule
from ...infrastructureServices.modules import RFIDModule
from ..dependencyInjection.get_sync_utils import SyncUtils
from ...infrastructureServices.repositories.RepositoryGateway import RepositoryGatewayImpl
from python.application.preferences import preferences_utils
from python.infrastructureServices.modules.RestModule import put_call


CONFIG_FILE_PATH = "./resources/device_config.json"


def get_remote_db_url():
    """
    Methods that returns the string url of the remote database
    :return: the string url of the remote database
    """
    return "https://intelligentbackpack-d463a-default-rtdb.europe-west1.firebasedatabase.app"


def initial_setup():
    preferences_utils.create_config_file(CONFIG_FILE_PATH)

    device_name = preferences_utils.get_device_id(CONFIG_FILE_PATH)
    primary_key = preferences_utils.get_device_key(CONFIG_FILE_PATH)
    username = preferences_utils.get_username(CONFIG_FILE_PATH)
    if device_name is None:
        raise ValueError('Device config file not found!')
    if primary_key is None:
        raise ValueError('Device config file not found!')
    if primary_key == "":
        register_request = {
            "url": "https://managebackpackservice.azurewebsites.net/addDevice/raspTest1",
            "payload": {

            }
        }
        response = put_call(register_request["url"], register_request["payload"])

        if response.status_code == "200" or response.status_code == 200:
            json_response = response.json()
            primary_key = json_response["authentication"]["symmetricKey"]["primaryKey"]
            preferences_utils.write_device_key(CONFIG_FILE_PATH, primary_key)

    return device_name, primary_key, username


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

        device_name, key, self.username = initial_setup()

        hub_thread = HubIoTModule.HubIotThread(self.sync_objects.queue_messages, device_name, key)
        rfid_thread = RFIDModule.RFIDReader(self.sync_objects.queue_messages)
        network_thread = RestModule.NetworkThread("Thread#Network", self.sync_objects.queue_requests)
        network_thread.setDaemon(True)

        self.repository = RepositoryGatewayImpl("db")
        self.repository.set_remote(get_remote_db_url(), self.sync_objects.queue_requests, device_name)

        self.modules = [hub_thread, network_thread, rfid_thread]

    def get_repository(self):
        """
        Getter method for the repository
        :return: the repository gateway
        """
        return self.repository

    def get_username(self):
        """
        Getter method for the username registered
        :return: the username registered
        """
        if self.username is None:
            return ""
        return self.username

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
