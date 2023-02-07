#Break beam sensor - look at breaking beam between emitter
#and receiver

#Imports
from machine import Pin
import time

beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.1)
    
    if beam.value() == 0:  #if beam is broken
        print("Beam Broken!")
       
    print("")