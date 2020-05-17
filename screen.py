import time  #增加时钟模块
import requests
from math import fabs
from base64 import b64encode
 
class RaspberryMonitorNetSpeed:
    url = 'http://192.168.1.1/update.cgi?output=netdev' 
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            # 'Connection':'keep-alive',
            'Connection': 'close',
            'Cookie': 'n56u_cookie_bw_rt_tab=WAN',
            'Host': '192.168.123.1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        }
    last_time = 0
    last_rbytes = 0
    last_tbytes = 0
 
    #构造函数初始化用户和密码等信息
    def __init__(self, username, passwd):
        self.headers['Authorization'] = 'Basic '+b64encode((username+':'+passwd).encode()).decode()
        data = self.__get_wan_rx_and_tx()
        self.last_rbytes = data[0]
        self.last_tbytes = data[1]
        self.last_time = data[2]
 
    def set_auth(self, username, passwd):
        self.headers['Authorization'] = 'Basic '+b64encode((username+':'+passwd).encode()).decode()
 
    def __get_wan_rx_and_tx(self):
        text = requests.get(self.url, headers=self.headers).text
        try:
            rx = int(text.split(',')[25].lstrip('rx:').strip(), 16)
            tx = int(text.split(',')[26].lstrip('tx:').rstrip('}\n').strip(), 16)
            new_time = time.time()
        except (IndexError, ValueError, TypeError):
            return False
        return [rx, tx, new_time]
 
    def __bytes_to_humanspeed(self, B):
        absval = fabs(B) / 1024
        megabyte = 1024
        gigabyte = megabyte * 1024
        terabyte = gigabyte * 1024
        # petabyte = terabyte * 1024
        if absval < megabyte:
            return str(round(absval, 2)) + ' KB/s'
        elif absval < gigabyte:
            return str(round(absval / megabyte, 2)) + ' M/s'
        else:
            return str(round(absval / gigabyte, 2)) + ' G/s'


    def get_human_speed(self):
        data = self.__get_wan_rx_and_tx()
        if data:
            down_speed = 0
            up_speed = 0
            try:
                down_speed = self.__bytes_to_humanspeed((data[0] - self.last_rbytes) / (data[2] - self.last_time))#返回下载速度信息
                up_speed = self.__bytes_to_humanspeed((data[1] - self.last_tbytes) / (data[2] - self.last_time))#上传速度信息
            except ZeroDivisionError:
                pass
            self.last_rbytes = data[0]
            self.last_tbytes = data[1]
            self.last_time = data[2]
            return down_speed, up_speed
 
    def get_bits_speed(self):
        data = self.__get_wan_rx_and_tx()
        if data:
            down_speed = self.__bytes_to_bitrate((data[0] - self.last_rbytes) / (data[2] - self.last_time))
            up_speed = self.__bytes_to_bitrate((data[1] - self.last_tbytes) / (data[2] - self.last_time))
            self.last_rbytes = data[0]
            self.last_tbytes = data[1]
            self.last_time = data[2]
            return down_speed, up_speed
 
    def __bytes_to_bitrate(self, B):
        bits = B * 8
        absval = fabs(bits)
        kilobit = 1000
        megabit = kilobit * 1000
        gigabit = megabit * 1000
        if absval < megabit:
            return str(round(bits / kilobit, 2)) + ' Kbps'
        elif absval < gigabit:
            return str(round(bits / megabit, 2)) + ' Mbps'
        else:
            return str(round(bits / gigabit, 2)) + ' Gbps'
 
#这里是主入口函数，初始化LCD1602等信息
if __name__ == '__main__':
    from lcd1602 import LCD1602
    a = RaspberryMonitorNetSpeed('username', 'password')
    lcd = LCD1602()
#不停的循环显示
    while True:
        tmp = a.get_human_speed()
        lcd.lcd_string('u:' + tmp[1], lcd.LCD_LINE_1)
        lcd.lcd_string('d:' + tmp[0], lcd.LCD_LINE_2)
        time.sleep(2)