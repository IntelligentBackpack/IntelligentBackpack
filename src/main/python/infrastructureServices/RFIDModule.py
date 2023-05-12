from time import sleep
from mfrc522 import SimpleMFRC522
import GPIO


class RFIDReader:
    def __init__(self, consumer):
        self.consumer = consumer
        self.reader = SimpleMFRC522()

    def startReading(self):
        try:
            while True:
                print("Hold a tag near the reader")
                id, text = self.reader.read()
                print("ID: %s\nText: %s" % (id, text))
                # execute the high order function
                self.consumer(id)
                sleep(5)
        except KeyboardInterrupt:
            GPIO.cleanup()
            raise
