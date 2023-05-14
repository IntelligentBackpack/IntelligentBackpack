import json
from ...RestModule import executeCalls
from ...RestModule import getCall
class RemoteRepositoryImpl:

    def __init__(self, serviceUrl, queue):
        self.serviceUrl = serviceUrl
        self.newRequest = {}
        self.queue = queue

    def addElement(self, value):
        self.newRequest = {
            "type": "PATCH",
            "url": self.serviceUrl + "/userName/zaino1/cavolo1.json",
            "payload": {
                str(value): "true"
            }
        }
        self.queue.put(self.newRequest)
        req = self.queue.get()
        element = json.loads(json.dumps(req))
        executeCalls(element["type"], element["url"], element["payload"])

    def removeElement(self, value):
        self.newRequest = {
            "type": "DELETE",
            "url": self.serviceUrl + "/userName/zaino1/cavolo1/" + str(value) + ".json",
            "payload": {}
        }
        self.queue.put(self.newRequest)
        req = self.queue.get()
        element = json.loads(json.dumps(req))
        executeCalls(element["type"], element["url"], element["payload"])
        return

    def findElement(self, value):
        response = getCall(self.serviceUrl + "/userName/zaino1/cavolo1/" + str(value) + ".json")
        return response.json() is not None