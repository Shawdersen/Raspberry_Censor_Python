import time
import RPi.GPIO as GPIO
class SoundDetect(object):
    def __init__(self):
        self.port = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.IN)

    def detect(self):
        while True:
            signal = GPIO.input(self.port)
            if signal == 1:
                print ("detect sound")
            else:
                print ("no sound")
            time.sleep(1)


if __name__ == "__main__":
    sound = SoundDetect()
    sound.detect()
