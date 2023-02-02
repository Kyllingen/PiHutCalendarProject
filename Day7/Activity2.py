#Basic motion sensing with PIR sensor
#Prints out message when motion is detected

#Imports
from machine import Pin, PWM
import time

#Set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up buzzer
buzzer = PWM(Pin(13))
buzzer.duty_u16(0)

#Set up sensor
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Allow sensor to settle on a baseline value
print("Warming up...")
time.sleep(10)
print("Sensor ready!")

#Alarm turns on volume, buzzes and flashes LEDs for 10 seconds
def alarm():
    buzzer.duty_u16(10000)
    
    for i in range(5):
        buzzer.freq(5000)
        
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(1)
        
        buzzer.freq(500)
        
        red.value(0)
        amber.value(0)
        green.value(0)
        
        time.sleep(1)
    
    buzzer.duty_u16(0)
    
while True:
    time.sleep(0.01)
    
    #Print motion detected, wait 5 seconds before detecting again
    if pir.value() == 1:
        print("I SEE YOU")
        
        alarm()
        
        print("Sensor active")