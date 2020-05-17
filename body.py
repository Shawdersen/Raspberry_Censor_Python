import RPi.GPIO as GPIO
import time
#初始化
def init():
    #设置不显示警告
    GPIO.setwarnings(False)
    #设置读取面板针脚模式
    GPIO.setmode(GPIO.BOARD)
    #设置读取针脚标号
    GPIO.setup(12,GPIO.IN)
    pass
 
def detct():
    while True:
        #当高电平信号输入时报警
        if GPIO.input(12) == True:
        	alart()
        else:
            continue
        time.sleep(3)
 
def alart():
    print(  " Someone is coming!")
 

time.sleep(2)
init()
detct()
GPIO.cleanup()
