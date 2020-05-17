import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GREEN = 18
YELLOW = 15
RED = 18
while True:
    t = 1
    if t == 1:
        GPIO.output(14, 1)
        GPIO.output(15, 1)
        GPIO.output(18, 1)
        time.sleep(0.5)
        t = 2
    if t == 2:
        GPIO.output(14, 1)
        GPIO.output(15, 0)
        GPIO.output(18, 0)
        time.sleep(0.5)
        t = 3
    if t == 3:
        GPIO.output(14, 0)
        GPIO.output(15, 1)
        GPIO.output(18, 0)
        time.sleep(0.5)
        t = 4
    if t == 4:
        GPIO.output(14, 0)
        GPIO.output(15, 0)
        GPIO.output(18, 1)
        time.sleep(0.5)
        t = 1
    pass
