#Playing with ball tilt sensor to signal when component goes over
#a certain angle when moved.
#Activates the buzzer when sensor is tilted

#Imports
from machine import Pin, PWM
import time

tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(13))
buzzer.freq(1000)

while True:
    
    time.sleep(0.01)
    
    if(tilt.value() == 1):
        print("*** TILT DETECTED ***")
        
        buzzer.duty_u16(10000)  #volume up
        time.sleep(0.2)
        buzzer.duty_u16(0)  	#volume down
        