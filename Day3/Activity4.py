#Testing OR with buttons and LEDS

#Imports
from machine import Pin
import time

#Set up button name and GPIO pin number + pin as input
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)

green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)
    
    if button1.value() == 1 or button2.value() == 1:
        print("Button 1 or 2 pressed")
        green.value(1)
        time.sleep(0.2)
        green.value(0)
        