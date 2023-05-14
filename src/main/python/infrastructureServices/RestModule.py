# ping the server and when the connection is on, i send the database update (insert or remove elements) with one call???
import requests
import time
from threading import Thread
import json

class NetworkThread (Thread):

    def __init__(self, nome, durata, cv, queue):
        Thread.__init__(self)
        self.nome = nome
        self.durata = durata
        self.cv = cv
        self.queue = queue

    def run(self):
        print("Thread '" + self.name + "' avviato")
        with self.cv:
            while(True):
                if self.queue.empty():
                    self.cv.wait()
                request = queue.get()
                element = json.loads(json.dumps(request))
                executeCalls(element["type"], element["url"], element["payload"])

        print("Thread '" + self.name + "' terminato")

def getCall(url):
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print("Error")
        print(e)

def executeCalls(type, url, payload):
    terminated = False
    while(not(terminated)):
        try:
            headers={'content-type': 'application/json'}
            if(type == "PATCH"):
                requests.patch(url, json.dumps(payload), headers=headers)
            elif(type == "DELETE"):
                requests.delete(url, headers=headers)
            terminated = True
            time.sleep(5)
        except Exception as e:
            print("Error")
            print(e)
