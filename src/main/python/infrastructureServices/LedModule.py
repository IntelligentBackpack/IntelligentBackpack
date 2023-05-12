from gpiozero import LED
from time import sleep


class RFIDReader:
    def __init__(self):
        self.led = LED(17)

    def singleLongLed(self):
        self.led.on()
        sleep(1000)
        self.led.off()
        sleep(1000)

    def tripleFastLed(self):
        i = 0
        while i < 3:
            self.led.on()
            sleep(100)
            self.led.off()
            sleep(100)
