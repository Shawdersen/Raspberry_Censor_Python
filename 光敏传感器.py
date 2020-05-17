
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
 
while True:
    print("sensor state %02x" % GPIO.input(18))
    time.sleep(1)
# while False:
#     print("false")