#Toggling all LEDs on Pico with buttons

#Imports
from machine import Pin
import time

#Set up button name and GPIO pin number + pin as input
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)
    
    if button1.value() == 1:
        green.toggle()
    if button2.value() == 1:
        amber.toggle()
    if button3.value() == 1:
        red.toggle()
        

        