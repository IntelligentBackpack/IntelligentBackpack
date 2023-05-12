# application service that use rfid module and network calls and repository
# from src.main.python.infrastructureServices import RestModule
# import importlib
# import asyncio
# import time
from python.infrastructureServices.repositories.RepositoryGateway import RepositoryGatewayImpl

'''
thread1 = RestModule.NetworkThread("Thread#1", 5)
thread1.start()
print("Ora")
print("Scrivo")
print("Cose")
thread1.join()
'''

if __name__ == "__main__":
    repo = RepositoryGatewayImpl()
