# ping the server and when the connection is on, i send the database update (insert or remove elements) with one call???
import requests
import time
from threading import Thread
import json
"""
Module that manage and send all the HTTP pending requests until the connection is available
"""

class NetworkThread (Thread):
    """
    Network thread that manages all the HTTP requests to be performed, using a synchronized queue
    to receive the requests to send and wait for.
    If the connection is not set or working, the requests are tried until the connection is on
    and the device ready to sent them
    """


    def __init__(self, name, queue):
        """
        Constructor method that create the thread object of this module
            Parameters:
                name (string): The name of the thread
                queue (queue): The synchronized queue used to receive all the requests to send

            Returns:
                void
        """
        Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        """
        Method that executes the thread
        """
        print("Thread '" + self.name + "' avviato")
        while (True):
            request = self.queue.get()
            element = json.loads(json.dumps(request))
            execute_calls(element["type"], element["url"], element["payload"])


def get_call(url):
    """
    Method that performs a HTTP GET request to the url received in input
        Parameters:
            url (string): The url to send the request

        Returns:
            response (object): response received from the request
    """
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print("Error")
        print(e)

def put_call(url, payload):
    """
    Method that performs HTTP PUT call requests to the url and with the payload received in input
    Parameters:
            url (string): The url to send the request
            payload (string): The payload to send inside the request

        Returns:
            void
    """
    try:
        headers = {'content-type': 'application/json'}
        response = requests.put(url, payload, headers=headers)
        return response
    except Exception as e:
        print("Error")
        print(e)

def execute_calls(type, url, payload):
    """
    Method that performs HTTP PATH or DELETE requests to the url and with the payload received in input
    Parameters:
            type (string): The type of the request to perform
            url (string): The url to send the request
            payload (string): The payload to send inside the request

        Returns:
            void
    """

    terminated = False
    while not (terminated):
        try:
            headers = {'content-type': 'application/json'}
            if type == "PATCH":
                requests.patch(url, json.dumps(payload), headers=headers)
            elif type == "DELETE":
                requests.delete(url, headers=headers)
            elif type == "PUT":
                requests.put(url, {},headers=headers)
            terminated = True
            time.sleep(5)
        except Exception as e:
            print("Error")
            print(e)
        time.sleep(10)
