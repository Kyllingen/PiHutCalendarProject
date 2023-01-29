#Play with analog to digital conversions

#Imports
from machine import ADC, Pin
import time

#Set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

while True:
    print(potentiometer.read_u16())
    
    time.sleep(1)