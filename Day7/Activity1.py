#Basic motion sensing with PIR sensor
#Prints out message when motion is detected

#Imports
from machine import Pin
import time

pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Allow sensor to settle on a baseline value
print("Warming up...")
time.sleep(10)

print("Sensor ready!")

while True:
    time.sleep(0.01)
    
    #Print motion detected, wait 5 seconds before detecting again
    if pir.value() == 1:
        print("I SEE YOU")
        
        time.sleep(5)
        
        print("Sensor active")