#Play with OLED display to show text
#Show a counter being refreshed on OLED display
#Based on having compiled and installed the ssd1306 library

#Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

#Setup I2C and pins used. Sleep for 1sec for initializing
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
time.sleep(1)

#Define display in pixels
display = SSD1306_I2C(128, 32, i2c)

counter = 0

while True:

    print(counter)
    # Clear display, fill text and then show it
    display.fill(0)

    display.text("The Endless", 0, 0)
    display.text("Counter", 0, 12)
    display.text((str(counter)), 56, 24)

    display.show();

    time.sleep(0.2)
    
    counter += 1