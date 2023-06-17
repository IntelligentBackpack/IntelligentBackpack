from time import sleep
from threading import Thread
try:
    from mfrc522 import SimpleMFRC522
    import RPi.GPIO as GPIO
except ImportError:
    pass

class RFIDReader(Thread):
    """
    Thread that manage the RFID module, listening all the cards passed near and send a new TAG_READ
    message to the synchronized queue for its management
    """

    def __init__(self, queue_messages):
        """
        Constructor method that create the thread object of this module
            Parameters:
                queue_messages (queue): The synchronized queue used to send the tag that the module read

            Returns:
                void
        """
        Thread.__init__(self)
        self.queue_messages = queue_messages
        self.reader = SimpleMFRC522()

    def run(self):
        """
        Method that executes the thread
        """
        try:
            while True:
                print("Hold a tag near the reader")
                id, text = self.reader.read()
                print("ID: %s\nText: %s" % (id, text))
                hex_value = str(hex(id))[2:10].upper()
                value_to_send = ":".join([hex_value[i:i+2] for i in range(0, len(hex_value), 2)])

                message_to_send = {
                    "type": "TAG_READ",
                    "payload": value_to_send
                }
                self.queue_messages.put(message_to_send)
                sleep(5)

        except KeyboardInterrupt:
            raise
        finally:
            GPIO.cleanup()
