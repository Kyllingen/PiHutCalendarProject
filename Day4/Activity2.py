#Play with analog potentiometer using red LED light
#Change the on/off interval using the potentiometer

#Imports
from machine import ADC, Pin
import time

#Set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

red = Pin(18, Pin.OUT)

myDelay = 1

while True:
    myDelay = potentiometer.read_u16() / 65000
    
    red.value(1)
    time.sleep(myDelay)
    
    red.value(0)
    time.sleep(myDelay)