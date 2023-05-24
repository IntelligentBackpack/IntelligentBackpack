# ping the server and when the connection is on, i send the database update (insert or remove elements) with one call???
import requests
import time
from threading import Thread
import json


class NetworkThread (Thread):

    def __init__(self, nome, queue):
        Thread.__init__(self)
        self.nome = nome
        self.queue = queue

    def run(self):
        print("Thread '" + self.name + "' avviato")
        while (True):
            request = self.queue.get()
            element = json.loads(json.dumps(request))
            execute_calls(element["type"], element["url"], element["payload"])


def get_call(url):
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print("Error")
        print(e)


def execute_calls(type, url, payload):
    terminated = False
    while not (terminated):
        try:
            headers = {'content-type': 'application/json'}
            if type == "PATCH":
                requests.patch(url, json.dumps(payload), headers=headers)
            elif type == "DELETE":
                requests.delete(url, headers=headers)
            terminated = True
            time.sleep(5)
        except Exception as e:
            print("Error")
            print(e)
        time.sleep(10)
