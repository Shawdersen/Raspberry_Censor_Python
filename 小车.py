import RPi.GPIO as GPIO
import time
#设置gpio口的模式
GPIO.setmode(GPIO.BOARD)
#定义信号接口gpio口
INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15
#设置gpio口为输出
GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)
#这里参考上一节模块接线的L298N模块的控制图
GPIO.output(INT1,GPIO.HIGH)
GPIO.output(INT2,GPIO.LOW)
GPIO.output(INT3,False)
GPIO.output(INT4,False)
#延时2秒之后执行cleanup释放GPIO接口
time.sleep(2)
GPIO.cleanup()