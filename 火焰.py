
import RPi.GPIO as GPIO
import time

DO = 4
GPIO.setmode(GPIO.BCM)
def setup():

    GPIO.setup(DO, GPIO.IN)

def Print(x):
    if x == 0:
        print ''
        print '   *********'
        print '   * Safe~ *'
        print '   *********'
        print ''
    if x == 1:
        print ''
        print '   *********'
        print '   * Fire! *'
        print '   *********'
        print ''

def loop():
    status = 1
    while True:
        tmp = GPIO.input(DO);
        if tmp != status:
            Print(tmp)
            status = tmp
        time.sleep(0.2)

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt: 
        pass 
