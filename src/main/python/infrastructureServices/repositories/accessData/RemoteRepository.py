from ...modules.RestModule import get_call


class RemoteRepositoryImpl:
    """
    Class that represents the remote repository, performing the requests to send to the remote
    database
    """
    def __init__(self, service_url, request_queue, hash):
        """
        Constructor method that create the object of this module
            Parameters:
                service_url (string): The name of the remote database
                request_queue (queue): The queue used to send HTTP requests directed to the remote database
                hash (string): The hash id of this device to which add or remove elements

            Returns:
                void
        """
        self.hash = hash
        self.service_url = service_url
        self.request_queue = request_queue

    def add_element(self, user, value):
        """
        Method that add an element into the remote database
            Parameters:
                user (string): The name of the user that own this device, to which save the added element
                value (string): The value to add into the remote record

            Returns:
                void
        """
        if user == "":
            return
        user = user.replace(".", "-")
        new_request = {
            "type": "PATCH",
            "url": self.service_url + "/" + user + "/" + self.hash + ".json",
            "payload": {
                str(value): True
            }
        }
        self.request_queue.put(new_request)

    def clear(self, user):
        if user == "":
            return
        user = user.replace(".", "-")
        new_request = {
            "type": "DELETE",
            "url": self.service_url + "/" + user + "/" + self.hash +  ".json",
            "payload": {

            }
        }
        self.request_queue.put(new_request)

    def remove_element(self, user, value):
        """
        Method that remove an element from the remote database
            Parameters:
                user (string): The name of the user that own this device, to which remove the element
                value (string): The value to remove from the remote database

            Returns:
                void
        """
        if user == "":
            return
        user = user.replace(".", "-")
        new_request = {
            "type": "DELETE",
            "url": self.service_url + "/" + user + "/" + self.hash + "/" + str(value) + ".json",
            "payload": {}
        }
        self.request_queue.put(new_request)
        return

    def find_element(self, user, value):
        """
        Method that find an element from the remote database
            Parameters:
                user (string): The name of the user that own this device, to which find the element
                value (string): The value to find from the repository

            Returns:
                result (boolean): return true if the element is present, false otherwise
        """
        if user == "":
            return
        user = user.replace(".", "-")
        response = get_call(self.service_url + "/" + user + "/" + self.hash + "/" + str(value) + ".json")
        return response.json() is not None
