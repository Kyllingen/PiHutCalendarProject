#Flash lights on and off every 0.5 seconds for "counter" no times

#Imports
from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1 #set counter to start at 1

while counter < 11:
    print(counter)
    
    red.value(1)
    amber.value(1)
    green.value(1)
    
    time.sleep(0.5)
    
    red.value(0)
    amber.value(0)
    green.value(0)
    
    time.sleep(0.5)
    
    counter += 1