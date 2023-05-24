# contains queue and cv instantiation
import queue


class SyncUtils:

    def __init__(self):
        self.queue_requests = queue.Queue()
        self.queue_messages = queue.Queue()
        pass

    def get_sync_queue(self):
        return self.queue_requests;

    def get_messages_queue(self):
        return self.queue_messages;
