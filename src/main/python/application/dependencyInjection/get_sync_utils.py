# contains queue and cv instantiation
import queue


class SyncUtils:
    """
    Class that contains all the synchronization utils needed for modules to synchronize themself
    and send messages
    """

    def __init__(self):
        """
        Constructor method that creates the requests and messages specific queues
        """
        self.queue_requests = queue.Queue()
        self.queue_messages = queue.Queue()
        pass

    def get_sync_queue(self):
        """
        Getter method that returns the requests queue

            Returns:
                queue_requests: the requests queue
        """
        return self.queue_requests

    def get_messages_queue(self):
        """
            Getter method that returns the messages queue

            Returns:
                queue_messages: the messages queue
        """
        return self.queue_messages
