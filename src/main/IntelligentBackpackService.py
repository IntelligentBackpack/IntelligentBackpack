# application service that use rfid module and network calls and repository
from python.infrastructureServices.repositories.RepositoryGateway import RepositoryGatewayImpl
from python.domainModel.domainServices.BackpackLogic import BackpackLogicService
from threading import Condition
from python.infrastructureServices.RestModule import NetworkThread
from python.infrastructureServices.RFIDModule import RFIDReader
import queue

def consumeTag(isbn, tag):
    print(tag)

if __name__ == "__main__":
    queue_requests = queue.Queue()
    repo = RepositoryGatewayImpl("https://intelligentbackpack-d463a-default-rtdb.europe-west1.firebasedatabase.app", queue_requests)
    domainLogic = BackpackLogicService(repo)
    manageTag = lambda tag : domainLogic.manageElement(tag)

    cv = Condition()
    rfid_thread = RFIDReader(manageTag, cv)
    network_thread = NetworkThread("Thread#Network", 5, cv)
    network_thread.start()
    rfid_thread.start()
    
    rfid_thread.join()
    network_thread.join()