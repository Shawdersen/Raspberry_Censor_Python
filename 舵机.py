
from gpiozero import PWMOutputDevice
from time import sleep

sg = PWMOutputDevice(pin=20, frequency=50)
angle = 30 #角度
duty = (10 / 180 * angle + 2.5) / 100
a.value = duty
sleep(1)