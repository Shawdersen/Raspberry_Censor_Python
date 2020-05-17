
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

INT1 = 11
INT2 = 13
INT3 = 15
INT4 = 16

GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)
#这里参考上一节模块接线的L298N模块的控制图
GPIO.output(INT1,GPIO.HIGH)
GPIO.output(INT2,GPIO.LOW)
GPIO.output(INT3,GPIO.HIGH)
GPIO.output(INT4,GPIO.LOW)
#延时2秒之后执行cleanup释放GPIO接口
time.sleep(0.5)
GPIO.cleanup()