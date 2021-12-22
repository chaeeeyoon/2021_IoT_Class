from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4
display = drivers.Lcd()


try:
        while True:
            h, t = Adafruit_DHT.read_retry(sensor, pin)
            
            now = datetime.datetime.now()
            if h is not None and t is not None:
                print('Temperature = %.1f*, Humidity = %.1f%%'%(t, h))
            else:
                print('Read Error')
            display.lcd_display_string(now.strftime("%x%X"),1)
            display.lcd_display_string("%.1f*C, %.1f%%"%(t, h),2)
finally: 
    display.lcd_clear()
