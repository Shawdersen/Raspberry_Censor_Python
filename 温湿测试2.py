import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
GPIO=18
humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)
if humidity is not None and temperature is not None:
   print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
else:
   print('Failed to get reading. Try again!')