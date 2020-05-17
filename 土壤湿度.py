#coding=utf-8
import RPi.GPIO as GPIO
import time
#针脚
channel = 18
GPIO.setmode(GPIO.BCM)
#定义针脚为input口
GPIO.setup(channel, GPIO.IN)    


#回调函数
def callback(channel):
    if GPIO.input(channel):
        print ('土壤有点干')
    else:
        print ('土壤太湿了')
        
 
#添加简单事件
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=200)
#添加时间触发的回调函数
GPIO.add_event_callback(channel, callback)

#保持主进程不退出
while True:
  time.sleep(0.1)
