#! /usr/bin/python

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x
from RPi import GPIO
from luma.lcd.aux import backlight


serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=24)
channel=18
light = backlight(gpio_LIGHT=channel, active_low=False)
light.enable(True)

device = pcd8544(serial,rotate=2)
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 10), "阿湘！", fill="red")
raw_input("Here")