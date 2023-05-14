from time import sleep
from mfrc522 import SimpleMFRC522
import GPIO
from threading import Thread


class RFIDReader(Thread):
    def __init__(self, consumer, cv):
        Thread.__init__(self)
        self.consumer = consumer
        self.reader = SimpleMFRC522()
        self.cv = cv

    def run(self):
        try:
            with self.cv:
                self.consumer(6)
                self.cv.wait()

                while True:
                    
                    print("Hold a tag near the reader")
                    id, text = self.reader.read()
                    print("ID: %s\nText: %s" % (id, text))
                    # execute the high order function
                    self.consumer(id)
                    self.cv.notifyAll()
                    sleep(5)

        except KeyboardInterrupt:
            GPIO.cleanup()
            raise
