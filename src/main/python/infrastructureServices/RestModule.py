# ping the server and when the connection is on, i send the database update (insert or remove elements) with one call???
import requests
import time
import asyncio
from threading import Thread


class NetworkThread (Thread):

    def __init__(self, nome, durata):
        Thread.__init__(self)
        self.nome = nome
        self.durata = durata

    def run(self):
        print("Thread '" + self.name + "' avviato")
        time.sleep(self.durata)
        print("Thread '" + self.name + "' terminato")


# must be async
async def performRequest():
    print("START CALL...")
    try:
        r = requests.get('http://echfo.jsontest.com/key/value/one/two')
        print(r.text)
    except Exception as e:
        print("Error: do another request, " + e)
        # await asyncio.sleep(5)
        time.sleep(5)
        print("Terminated wait, try another")


async def a_main():
    print("Hey")
    # Anything else to run
    while (True):
        # from python 3.7, asyncio.create_task(...)
        task = asyncio.ensure_future(performRequest())
        # wait for the task to complete
        await task
        break


async def executeCalls():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(a_main())
