import RPi.GPIO as GPIO
import time
 
channel = 21                          #引脚号14

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while(1):
  if(GPIO.input(channel)==0):
    print('yes') 
    time.sleep(0.5)
  else:
      print("no")
      time.sleep(0.5)
GPIO.cleanup()