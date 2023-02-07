#Playing with ball tilt sensor to signal when component goes over
#a certain angle when moved.
#Count the number of times sensor is tilted 

#Imports
from machine import Pin
import time

tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)
tiltCount = 0
state = 0

while True:
    
    time.sleep(0.1)
    print(tilt.value())
    #if tilted and not already tilting, count
    if state == 0 and tilt.value() == 1:
        tiltCount += 1
        state = 1
        print("tilts = ", tiltCount)
        
    #if not tilting anymore, reset state
    if state == 1 and tilt.value() == 0:
        state = 0
        