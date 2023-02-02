#Simple light sensing using LEDs to check values as
#a percentage between 0 (no light) to 100 (max light) 
#Shine light / turn off light and run code to see changes

#imports
from machine import ADC, Pin
import time

#Set up LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

lightsensor = ADC(Pin(26))


while True:
    
    light = lightsensor.read_u16()

    lightpercent = round(light / 65535 * 100, 1)

    print(str(lightpercent) + "%")
    
    time.sleep(1)
    
    if lightpercent <= 30:
        red.value(1)
        amber.value(0)
        green.value(0)
        
    elif 30 < lightpercent < 60:
        red.value(0)
        amber.value(1)
        green.value(0)
    else:
        red.value(0)
        amber.value(0)
        green.value(1)
        
