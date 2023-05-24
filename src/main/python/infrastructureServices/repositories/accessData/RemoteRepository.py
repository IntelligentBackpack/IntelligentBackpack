from python.infrastructureServices.modules.RestModule import get_call


class RemoteRepositoryImpl:

    #TODO serve email e hash
    def __init__(self, service_url, request_queue, hash):
        self.hash = hash
        self.service_url = service_url
        self.request_queue = request_queue

    def add_element(self, user, value):
        if user is "":
            return
        print("AGGIUNGO ELEMENTO DA INVIARE")
        new_request = {
            "type": "PATCH",
            "url": self.service_url + "/" + user + "/" + self.hash + ".json",
            "payload": {
                str(value): "true"
            }
        }
        self.request_queue.put(new_request)
        # req = self.request_queue.get()
        # element = json.loads(json.dumps(req))
        # execute_calls(element["type"], element["url"], element["payload"])

    def remove_element(self, user, value):
        if user is "":
            return
        new_request = {
            "type": "DELETE",
            "url": self.service_url + "/" + user + "/" + self.hash + "/" + str(value) + ".json",
            "payload": {}
        }
        self.request_queue.put(new_request)
        # req = self.request_queue.get()
        # element = json.loads(json.dumps(req))
        # execute_calls(element["type"], element["url"], element["payload"])
        return

    def find_element(self, user, value):
        if user is "":
            return
        response = get_call(self.service_url + "/" + user + "/" + self.hash + "/" + str(value) + ".json")
        return response.json() is not None
