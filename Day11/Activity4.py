#Play with OLED display to show text
#Naughty or nice game. Hit the button at the right time
#Based on having compiled and installed the ssd1306 library

#Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

#Set up button
button = Pin(8, Pin.IN, Pin.PULL_DOWN)

#Setup I2C and pins used. Sleep for 1sec for initializing
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
time.sleep(1)

#Define display in pixels
display = SSD1306_I2C(128, 32, i2c)

state = 0

while True:

    time.sleep(0.2)
    
    display.fill(0)
    
    if state == 0:

        display.text("Naughty or Nice?", 0, 0)
        display.text("->Naughty Nice  ", 0, 24)

        display.show();
        
        state = 1
        
        if button.value() == 1:
            display.fill(0)
            display.text("Oh no!", 0,0)
            display.text("->Naughty Nice  ", 0, 24)
            
            display.show()
                
            time.sleep(2.0)
    else:
        display.text("Naughty or Nice?", 0, 0)
        display.text("  Naughty Nice<-", 0, 24)
        
        display.show()
        
        state = 0
        
        if button.value() == 1:
            display.fill(0)
            display.text("Yay!", 0,0)
            display.text("  Naughty Nice<-", 0, 24)
            
            display.show()
                
            time.sleep(2.0)
