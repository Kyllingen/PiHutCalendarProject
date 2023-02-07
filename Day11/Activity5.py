#Play with OLED display to show text
#Display continous light readings from light sensor
#Based on having compiled and installed the ssd1306 library

#Imports
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time


#Setup I2C and pins used. Sleep for 1sec for initializing
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
time.sleep(1)

#Define display in pixels
display = SSD1306_I2C(128, 32, i2c)


lightSensor = ADC(Pin(26))

while True:

    time.sleep(0.5)
    
    light = round((lightSensor.read_u16())/65535*100, 1)
    
    print(light)
    
    display.fill(0)
    
    display.text("Light level:", 0,0)
    display.text((str(light) + "%"),0,12)
    
    display.show()